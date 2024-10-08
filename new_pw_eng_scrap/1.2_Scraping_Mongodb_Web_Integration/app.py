from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import logging
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pymongo.mongo_client import MongoClient
from pymongo.errors import DuplicateKeyError 

# Logging setup
logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

# Configure Selenium WebDriver
chrome_driver_path = "C:/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Update this with your path

@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Extract the search string from the form and clean it
            searchString = request.form['content'].replace(" ", "")
            flipkart_url = f"https://www.flipkart.com/search?q={searchString}"

            # Set up Selenium WebDriver
            service = Service(chrome_driver_path)
            driver = webdriver.Chrome(service=service)
            driver.get(flipkart_url)

            # Wait for the page to load completely
            driver.implicitly_wait(10)
            page_source = driver.page_source
            flipkart_html = bs(page_source, "html.parser")

            # Extract the product links
            items = flipkart_html.find_all("div", {"class": "cPHDOP col-12-12"})

            if len(items) == 0:
                logging.error("No products found with the specified class.")
                driver.quit()
                return "No products found."

            del items[0:3]  # Skip irrelevant items, if any

            if len(items) == 0:
                logging.error("Not enough products found after filtering.")
                driver.quit()
                return "Not enough products found."

            product_link = "https://www.flipkart.com" + items[0].div.div.div.a['href']

            # Open the product page
            driver.get(product_link)
            time.sleep(5)

            # Scroll down to load reviews (if necessary)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            # Get the page source again after loading reviews
            page_source = driver.page_source
            product_html = bs(page_source, "html.parser")

            # Scrape the reviews, ratings, and person names
            reviews = product_html.find_all("div", {"class": "ZmyHeo"})  # Review text
            ratings = product_html.find_all("div", {"class": "XQDdHH Ga3i8K"})  # Ratings
            persons = product_html.find_all("p", {"class": "_2NsDsF AwS1CA"})  # Person name

            if not reviews or not ratings or not persons:
                logging.error("Failed to scrape reviews, ratings, or persons.")
                return "Could not fetch reviews."

            review_list = []
            for review, rating, person in zip(reviews, ratings, persons):
                review_dict = {
                    "Product": searchString,
                    "Review": review.text.strip(),
                    "Rating": rating.text.strip(),
                    "Person": person.text.strip()
                }
                review_list.append(review_dict)

            # MongoDB connection and insertion
            uri = "mongodb+srv://pwskills:pwskills@cluster0.hbbfbmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            client = MongoClient(uri)
            db = client['scrapper_eng_pwskills']
            coll_pw_eng = db['scraper_pwskills_eng']
            # coll_pw_eng.insert_many(review_list)

        
             # Try inserting data if it doesn't exist
            for review_data in review_list:
                try:
                    # Check if the review already exists in MongoDB (based on review text and person name)
                    if not coll_pw_eng.find_one({"Review": review_data["Review"], "Person": review_data["Person"]}):
                        coll_pw_eng.insert_one(review_data)
                    else:
                        logging.info(f"Review by {review_data['Person']} already exists in the database.")
                except DuplicateKeyError as e:
                    logging.error(f"Duplicate key error: {e}")

            # Close the Selenium driver
            driver.quit()

            # Render the results page
            return render_template('result.html', reviews=review_list)

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return f"Something went wrong: {e}"

    else:
        return render_template('index.html')


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=False)

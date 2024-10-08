
# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS, cross_origin
# import logging
# import pymongo
# from bs4 import BeautifulSoup as bs
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# logging.basicConfig(filename="scrapper.log", level=logging.INFO)

# app = Flask(__name__)

# # Configure Selenium WebDriver
# chrome_driver_path = "C:/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Update this with your path

# @app.route("/", methods=['GET'])
# def homepage():
#     return render_template("index.html")

# @app.route("/review", methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         try:
#             # Extract the search string from the form and clean it
#             searchString = request.form['content'].replace(" ", "")
#             flipkart_url = "https://www.flipkart.com/search?q=" + searchString

#             # Set up Selenium WebDriver
#             service = Service(chrome_driver_path)
#             driver = webdriver.Chrome(service=service)
#             driver.get(flipkart_url)

#             # Wait for the page to load completely
#             driver.implicitly_wait(10)
#             page_source = driver.page_source
#             flipkart_html = bs(page_source, "html.parser")

#             # Extract the product links (replace with the right class name if different)
#             items = flipkart_html.find_all("div", {"class": "cPHDOP col-12-12"})

#             if len(items) == 0:
#                 print("No products found with the specified class.")
#                 driver.quit()
#                 exit()

#             del items[0:3]  # Skip irrelevant items, if any

#             if len(items) == 0:
#                 print("Not enough products found after filtering.")
#                 driver.quit()
#                 exit()

#             product_link = "https://www.flipkart.com" + items[0].div.div.div.a['href']

#             # product_link = "https://www.flipkart.com" + box.div.div.div.a['href']

#             # Open the product page
#             driver.get(product_link)
#             time.sleep(5)

#             # Scroll down to load reviews (if necessary)
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(3)

#             # Get the page source again after loading reviews
#             page_source = driver.page_source
#             product_html = bs(page_source, "html.parser")

#             # Scrape the reviews, ratings, and person names
#             reviews = product_html.find_all("div", {"class": "ZmyHeo"})  # Review text
#             ratings = product_html.find_all("div", {"class": "XQDdHH Ga3i8K"})  # Ratings
#             persons = product_html.find_all("p", {"class": "_2NsDsF AwS1CA"})  # Person name

#             review_list = []
#             for review, rating, person in zip(reviews, ratings, persons):
#                 review_dict = {
#                     "Product": searchString,
#                     "Review": review.text.strip(),
#                     "Rating": rating.text.strip(),
#                     "Person": person.text.strip()
#                 }
#                 review_list.append(review_dict)

#             # first create a connection to the MongoDB instance running on MongoDB Atlas
#             # python -m pip install "pymongo[srv]==3.6"
            
#             from pymongo.mongo_client import MongoClient

#             # uri = "mongodb+srv://pwskills:<db_password>@cluster0.hbbfbmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#             uri = "mongodb+srv://pwskills:pwskills@cluster0.hbbfbmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#             # uri="mongodb+srv://pwskills:pwskills@cluster0.hbbfbmr.mongodb.net/?retryWrites=true&w=majority"
#             # Create a new client and connect to the server
#             client = MongoClient(uri)
#             db = client['scrapper_eng_pwskills']
#             coll_pw_eng = db['scraper_pwskills_eng']
#             coll_pw_eng.insert_many(review_list)

#             # Send a ping to confirm a successful connection
#             try:
#                 client.admin.command('ping')
#                 print("Pinged your deployment. You successfully connected to MongoDB!")
#             except Exception as e:
#                 print(e)
#             # Save to MongoDB
#             # client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.ln0bt5m.mongodb.net/?retryWrites=true&w=majority")

#             # Quit the Selenium driver
#             driver.quit()

#             # Render the results page
#             return render_template('result.html', reviews=review_list)

#         except Exception as e:
#             logging.error(f"Error occurred: {e}")
#             print(f"Error occurred: {e}")  # Print the exact error for debugging
#             return 'Something went wrong'


#     else:
#         return render_template('index.html')


# if __name__ == "__main__":
#     print("Starting Flask server...")
#     app.run(host="127.0.0.1", port=5000, debug=False)




# from flask import Flask, render_template, request
# from flask_cors import CORS, cross_origin
# import logging
# from bs4 import BeautifulSoup as bs
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from pymongo.mongo_client import MongoClient

# # Logging setup
# logging.basicConfig(filename="scrapper.log", level=logging.INFO)

# app = Flask(__name__)

# # Configure Selenium WebDriver
# chrome_driver_path = "C:/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Update this with your path

# @app.route("/", methods=['GET'])
# def homepage():
#     return render_template("index.html")

# @app.route("/review", methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         try:
#             # Extract the search string from the form and clean it
#             searchString = request.form['content'].replace(" ", "")
#             flipkart_url = f"https://www.flipkart.com/search?q={searchString}"

#             # Set up Selenium WebDriver
#             service = Service(chrome_driver_path)
#             driver = webdriver.Chrome(service=service)
#             driver.get(flipkart_url)

#             # Wait for the page to load completely
#             driver.implicitly_wait(10)
#             page_source = driver.page_source
#             flipkart_html = bs(page_source, "html.parser")

#             # Extract the product links
#             items = flipkart_html.find_all("div", {"class": "cPHDOP col-12-12"})

#             if len(items) == 0:
#                 logging.error("No products found with the specified class.")
#                 driver.quit()
#                 return "No products found."

#             del items[0:3]  # Skip irrelevant items, if any

#             if len(items) == 0:
#                 logging.error("Not enough products found after filtering.")
#                 driver.quit()
#                 return "Not enough products found."

#             product_link = "https://www.flipkart.com" + items[0].div.div.div.a['href']

#             # Open the product page
#             driver.get(product_link)
#             time.sleep(5)

#             # Scroll down to load reviews (if necessary)
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(3)

#             # Get the page source again after loading reviews
#             page_source = driver.page_source
#             product_html = bs(page_source, "html.parser")

#             # Scrape the reviews, ratings, and person names
#             reviews = product_html.find_all("div", {"class": "ZmyHeo"})  # Review text
#             ratings = product_html.find_all("div", {"class": "XQDdHH Ga3i8K"})  # Ratings
#             persons = product_html.find_all("p", {"class": "_2NsDsF AwS1CA"})  # Person name

#             if not reviews or not ratings or not persons:
#                 logging.error("Failed to scrape reviews, ratings, or persons.")
#                 return "Could not fetch reviews."

#             review_list = []
#             for review, rating, person in zip(reviews, ratings, persons):
#                 review_dict = {
#                     "Product": searchString,
#                     "Review": review.text.strip(),
#                     "Rating": rating.text.strip(),
#                     "Person": person.text.strip()
#                 }
#                 review_list.append(review_dict)

#             # MongoDB connection and insertion
#             uri = "mongodb+srv://pwskills:pwskills@cluster0.hbbfbmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#             client = MongoClient(uri)
#             db = client['scrapper_eng_pwskills']
#             coll_pw_eng = db['scraper_pwskills_eng']
#             coll_pw_eng.insert_many(review_list)

#             # Close the Selenium driver
#             driver.quit()

#             # Render the results page
#             return render_template('result.html', reviews=review_list)

#         except Exception as e:
#             logging.error(f"Error occurred: {e}")
#             return f"Something went wrong: {e}"

#     else:
#         return render_template('index.html')


# if __name__ == "__main__":
#     print("Starting Flask server...")
#     app.run(host="127.0.0.1", port=5000, debug=False)



from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import logging
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pymongo.mongo_client import MongoClient

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
            coll_pw_eng.insert_many(review_list)

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








































# previous code for reference, not working due to flipkart changes 

# from flask import Flask, render_template, request,jsonify
# from flask_cors import CORS,cross_origin
# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen as uReq
# import logging
# import pymongo
# logging.basicConfig(filename="scrapper.log" , level=logging.INFO)

# app = Flask(__name__)

# @app.route("/", methods = ['GET'])
# def homepage():
#     return render_template("index.html")

# @app.route("/review" , methods = ['POST' , 'GET'])
# def index():
#     if request.method == 'POST':
#         try:
#             searchString = request.form['content'].replace(" ","")
#             flipkart_url = "https://www.flipkart.com/search?q=" + searchString
#             uClient = uReq(flipkart_url)
#             flipkartPage = uClient.read()
#             uClient.close()
#             flipkart_html = bs(flipkartPage, "html.parser")
#             bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
#             del bigboxes[0:3]
#             box = bigboxes[0]
#             productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
#             prodRes = requests.get(productLink)
#             prodRes.encoding='utf-8'
#             prod_html = bs(prodRes.text, "html.parser")
#             print(prod_html)
#             commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

#             filename = searchString + ".csv"
#             fw = open(filename, "w")
#             headers = "Product, Customer Name, Rating, Heading, Comment \n"
#             fw.write(headers)
#             reviews = []
#             for commentbox in commentboxes:
#                 try:
#                     #name.encode(encoding='utf-8')
#                     name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

#                 except:
#                     logging.info("name")

#                 try:
#                     #rating.encode(encoding='utf-8')
#                     rating = commentbox.div.div.div.div.text


#                 except:
#                     rating = 'No Rating'
#                     logging.info("rating")

#                 try:
#                     #commentHead.encode(encoding='utf-8')
#                     commentHead = commentbox.div.div.div.p.text

#                 except:
#                     commentHead = 'No Comment Heading'
#                     logging.info(commentHead)
#                 try:
#                     comtag = commentbox.div.div.find_all('div', {'class': ''})
#                     #custComment.encode(encoding='utf-8')
#                     custComment = comtag[0].div.text
#                 except Exception as e:
#                     logging.info(e)

#                 mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
#                           "Comment": custComment}
#                 reviews.append(mydict)
#             logging.info("log my final result {}".format(reviews))

            
#             client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.ln0bt5m.mongodb.net/?retryWrites=true&w=majority")
#             db =client['scrapper_eng_pwskills']
#             coll_pw_eng = db['scraper_pwskills_eng']
#             coll_pw_eng.insert_many(reviews)

#             return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
#         except Exception as e:
#             logging.info(e)
#             return 'something is wrong'
#     # return render_template('results.html')

#     else:
#         return render_template('index.html')


# if __name__ == "__main__":
#     print("Starting Flask server...")
#     app.run(host="127.0.0.1", port=5000, debug=False)

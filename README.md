# Web-Scrape and Image Scraping
This repository contains the work I've done as part of the Data Science Master's course by PwSkills, with personal variations on Selenium(for web scraping). The main focus of this project is collecting data from websites, and it includes tasks such as scraping reviews, ratings and reviewer's name and automating image extraction form websites.

# Project Overview

## 1. Image Scraping
Image scraping is the process of extracting images from websites automatically. This project demonstrates how to create a Python-based image scraper using Flask as the web framework, BeautifulSoup for parsing HTML, and Requests for making HTTP requests. The application allows users to input a search query, scrapes images based on that query from the web, stores them locally, and then displays them on a results page.

### - Key Technologies
`Python:` Core language for scripting and backend logic. <br>
`Flask:` A lightweight web framework to handle the user interface, form submissions, and routing.<br>
`BeautifulSoup:` Library used for parsing HTML and extracting image URLs.<br>
Requests: To fetch web content and download images.<br>
`MongoDB:` Used to store metadata related to the scraped images (optional, depending on implementation).<br>
`HTML/CSS:` Frontend for displaying input forms and results.<br>
### - Features
- **User Input Form:** A simple search form where users can enter a search term (e.g., "ISRO").
- **Web Scraping:** Once the form is submitted, the application scrapes images from a Google search based on the user input.
- **Image Storage:** Scraped images are saved to a local images/ directory for further use.
- **MongoDB Integration:** Scraped images' binary data (in Base64 format) and metadata are stored in a MongoDB database.
### How it Works
- User Input: A user enters a query (like “ISRO”) into a search form hosted on the homepage.
- Web Request: The query triggers a web request to Google Images via the Requests library.
- Scraping: The BeautifulSoup library parses the returned HTML, searching for image tags (<img>), and retrieves the image URLs.
- Image Download: The images are downloaded from the URLs and saved in the images/ folder on your local machine.
- MongoDB Integration: The scraped images' metadata (e.g., id,index, and image Base64 data) is stored in a MongoDB database.


# 2. Web Scraper for Flipkart Product Reviews

This project is a fully functional web-based scraper that retrieves product reviews from Flipkart, displays them on a web page, and stores the collected data into MongoDB. It is divided into two phases: initial scraping and web integration with MongoDB.


### Phase 1: Initial Scraping (1.1_Flipkart_initial_scraping)
In this phase, we focus on **basic web scraping** using `Selenium` and `BeautifulSoup`. The scraper targets Flipkart product pages and extracts:
- Product reviews
- Ratings
- Reviewer names

The initial scraping process is demonstrated in the Jupyter notebook (`Web_Scraping_flipkart.ipynb`), showing how the data is retrieved programmatically.

### Phase 2: Web Scraping with MongoDB Integration (1.2_Scraping_Mongodb_Web_Integration)

#### Web Interface Creation
In this phase, the scraping functionality is integrated into a web application. A user-friendly interface is developed using **HTML** and **CSS**:
- **Index page** (`index.html`): Users can input a product name.
- **Results page** (`result.html`): Displays the scraped reviews and ratings in a tabular format.

#### Scraping and Inserting Data into MongoDB
- Once a product search is initiated from the web interface, the scraper navigates to the product's Flipkart page, extracts the reviews, ratings, and reviewer details, and inserts this data into MongoDB.
- The scraping and MongoDB insertion logic is handled in `app.py`, while logs of the scraping process are saved in `scrapper.log`.

#### Retrieving and Storing Data
- The `demo.py` script fetches the reviews stored in MongoDB and exports them into a CSV file (`mongodb_collections.csv`), demonstrating how the data can be retrieved and processed for further analysis.
## How to Set Up and Run the Project

Follow these steps to clone the repository, set up the environment, and run the web scraper:

### Step 1: Clone the Repository
First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/your-repository-name.git
```
### Step 2: Install Dependencies
Navigate into the project folder and install the required Python packages:
```bash
cd NEW_PW_WND_SCRAP/1.1_Flipkart_initial_scraping
pip install -r requirements.txt

cd ../1.2_Scraping_Mongodb_Web_Integration
pip install -r requirements.txt
```
### Step 3: Set Up MongoDB
Make sure you have MongoDB installed and running on your local machine or have access to a MongoDB Atlas instance. You can configure the MongoDB connection URI in app.py.

### Step 4: Run the Web Application
To start the web application, python app.py:

```bash
python app.py
```
The application will be hosted locally on http://127.0.0.1:5000. Open this URL in your browser to access the web interface.

### Step 5: Scraping and Inserting Data
On the homepage, enter the product name you wish to search on Flipkart. The app will scrape the product reviews and ratings, display them in a table, and save the data to MongoDB.

### Step 6: Retrieving Data from MongoDB
To export the stored data into a CSV file, run the demo.py script:

```bash
python demo.py
```
This will save the reviews in **mongodb_collections.csv**
<br>
<br>
<hr>
<br>

> **Note:**  The class name of product keeps changing so you need to update the class name in the code according to the website and product you are scraping.
<br>

> **Note:**  The files such as tv.csv, mobile.csv, laptop.csv are the files generatedd automatically whenever we run the code and search for the product.

>` **!IMPORTANT!** `: This project is for educational purposes only. The data scraped from the website is not used for any commercial purposes and is only used for learning and practicing web scraping techniques, there is no intention to harm the website or the company policy in any way.


## Project Structure
```bash
/Image_Scraping/
|
|---/Image-Scraper-Selenium-main/Image-Scraper-Selenium-main
|   |---app.py
|   |--- image.png
|   |--- scrapper.log
|   |--- requirements.txt
|   |--- /static/
|   |   |--- /css/
|   |       |--- main.css
|   |       |--- style.css
|   |--- /templates/
|   |   |--- base.html
|   |   |--- index.html
|   |   |--- result.html
|   |--- /images/
|--- /images/
|--- /raw_img_scrap_code.ipynb  
|
NEW_PW_WND_SCRAP
|
|--- 1.1_Flipkart_initial_scraping
|       |
|       |--- requirements.txt
|       |--- README.md
|       |--- Web_Scraping_flipkart.ipynb
|
|--- 1.2_Scraping_Mongodb_Web_Integration
|       |
|       |--- static
|       |     |
|       |     |--- css
|       |           |--- main.css
|       |           |--- style.css
|       |
|       |--- templates
|       |     |--- base.html
|       |     |--- index.html
|       |     |--- result.html
|       |
|       |--- app.py
|       |--- demo.py
|       |--- requirements.txt
|       |--- scrapper.log
|       |--- test_file.py
|       |--- mongodb_collections.csv

________________________________________________
```
### Summary
This project allows you to:

- Scrape product reviews and ratings from Flipkart.
- Display the scraped data on a web page.
- Store the data into MongoDB for future use.
- Retrieve and export the stored data into a CSV file for analysis.
Feel free to fork the repository or use it as a starting point for building more advanced web scraping and data integration projects!

>`LICENSE`: <br>
This project is licensed under the MIT License - see the LICENSE file for details.

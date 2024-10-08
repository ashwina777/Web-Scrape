# WebScraper
 I have developed scripts to scrape websites for reviews, ratings, and other relevant data
# Flipkart Web Scraping Project

## Project Overview

This project focuses on scraping product reviews from Flipkart, particularly the **reviewer's name**, **rating**, and **review (comment)**. The project initially started with simple web scraping techniques but evolved to use Selenium when Flipkart began restricting scraping. 

### Key Features:
- **Extracts reviews, ratings, and reviewer names** from Flipkart product pages.
- Two approaches for web scraping:
  1. **Basic Web Scraping**: Using `requests` and `BeautifulSoup` when scraping was allowed.
  2. **Selenium with ChromeDriver**: Used when scraping was restricted and required interaction with dynamically loaded content.

## Data Extracted
For each review, the following data is collected:
1. **Reviewer Name**: The person who posted the review.
2. **Rating**: The rating given by the reviewer (out of 5 stars).
3. **Review (Comment)**: The actual text of the review.

## Approaches Used

### Approach 1: Simple Web Scraping (Initial Phase)
Initially, Flipkart allowed access to its HTML content, which made scraping simple. In this phase:
- We used the **requests** library to fetch the HTML content of the page.
- **BeautifulSoup** was used to parse the HTML and extract key data like reviewer names, ratings, and comments.
 ###  Approach 2: Selenium with ChromeDriver (Later Phase)
  - Automated scraping using Selenium and ChromeDriver when scraping was later restricted by Flipkart.
    - **Selenium** was used to automate the process of clicking buttons and loading more reviews.
    - **ChromeDriver** was used to control the Chrome browser.

## Installation

Follow the steps below to set up and run the project on your local machine:

### 1. Clone the Repository
First, you need to clone the repository to your local machine. Open your terminal (or command prompt) and run the following commands:

```bash
git clone https://github.com/ashwina777/WebScraper.git
cd WebScraper/Flipkart
```
### 2. Install Python Libraries
After cloning the repository, install the required dependencies using the `requirements.txt` file. This ensures that all necessary libraries (like `requests`, `beautifulsoup4`, and `selenium`) are installed:

```bash
pip install -r requirements.txt
```
### 3. Download and Install ChromeDriver
Since the project uses Selenium to interact with a browser, you'll need `ChromeDriver` to automate Chrome. Follow these steps to download and install ChromeDriver:

- **Step 1**: **Download ChromeDriver**
Visit the ChromeDriver official site.
Select the version that matches your current version of Google Chrome.
To check your Chrome version, open Chrome and go to chrome://settings/help.
The version number will be listed there.
- **Step 2**: **Install ChromeDriver**
Once you've downloaded ChromeDriver, extract the file.
Move the chromedriver executable to a location on your system where it can be easily accessed, such as /usr/local/bin for macOS/Linux or a preferred directory on Windows.
- **Step 3**: **Add ChromeDriver to Your System PATH**
<br>For Windows:
Right-click on "This PC" or "My Computer" and select Properties.
Click on Advanced system settings and then on Environment Variables.
Under System variables, find the Path variable, select it, and

>`Note`:  The class name of product keeps changing so you need to update the class name in the code according to the website and product you are scraping. 

### File Structure
```bash
WebScraper
|
|--- Flipkart_initial_scraping
|       |
|       |---- requirements.txt
|       |---- README.md
|       |---- Web_Scraping_flipkart.ipynb
|
|--- README.md
```


>`LICENSE`: <br>
This project is licensed under the MIT License - see the LICENSE file for details.

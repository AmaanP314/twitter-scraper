Twitter Scraper:

This project aims to scrape tweets from Twitter using Selenium, a powerful automation tool for web browsers, and Python. It extracts data from the Twitter website, including usernames and tweet texts, and stores them in a CSV file for further analysis.

Features:

Logs into Twitter using provided credentials.
Scrapes tweets from the Twitter timeline.
Handles dynamic loading of tweets by scrolling the page.
Utilizes explicit waits for robust and efficient automation.
Supports custom user-agent configuration for browser emulation.
Requirements
Python 3.x
Selenium
Pandas

Logic:

  Importing Necessary Modules: The script begins by importing the required modules, including Selenium for web automation, Pandas for data handling, and other utilities for working with web elements.
  
  Setting Up WebDriver and Options: It sets up the Chrome WebDriver with specific options, such as setting a custom user agent to emulate a mobile device.
  
  Logging into Twitter: It navigates to the Twitter login page, enters the username and password, and clicks the login button using explicit waits to ensure elements are clickable and visible.
  
  Scraping Tweets: Once logged in, the script enters a loop to scroll through the Twitter timeline, scraping tweet elements using explicit waits to ensure elements are present before extraction. It extracts the username and tweet text from each tweet element.
  
  Handling Dynamic Loading: The script dynamically loads tweets by scrolling the page to the bottom and waiting for new tweets to appear, ensuring all tweets are captured.
  
  Storing Data: It stores the scraped data (usernames and tweet texts) in lists and then creates a Pandas DataFrame from these lists. Finally, it saves the DataFrame to a CSV file for further analysis.
  
  Closing WebDriver: After scraping is complete, the WebDriver is closed to release system resources.

Usage:

Clone or download the repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Set up the path to the Chrome WebDriver executable in the script.
Provide your Twitter username and password in the script.
Run the script.
The scraped tweets will be saved to a CSV file named tweets-all.csv in the specified directory.

Note:

Ensure that you have the latest version of Chrome installed on your system.

Make sure to configure the path to the Chrome WebDriver executable correctly.

The structure of the Twitter website may change in the future, affecting the functionality of the scraper. XPath expressions used to locate elements may become outdated or invalid. Regular maintenance and updates to the scraper may be necessary to accommodate such changes.If you encounter such results feel free to inform me or modify the code as per the requirement

Use this scraper responsibly and respect Twitter's terms of service and rate limits.

Contributor:
Amaan Poonawala

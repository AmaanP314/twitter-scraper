# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# URL of the Twitter login page
web = "https://twitter.com/"

# Path to the chromedriver executable
path = r"C:\Users\Hannan Poonawala\OneDrive\Desktop\AMAAN\WebScrape\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Initialize the Chrome options
chrome_options = Options()

# Set the desired user agent
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")


# Initialize the Chrome driver with options
driver = webdriver.Chrome(executable_path=path, options=chrome_options)

# Open the Twitter login page
driver.get(web)

# Maximize the browser window
driver.maximize_window()

# Set an implicit wait time for the driver
driver.implicitly_wait(10)

################# LOGIN #################

# Wait for the bottom bar button to be clickable and click it
bottom_bar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="BottomBar"]//button')))
bottom_bar.click()

# Wait for the login link to be clickable and click it
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/login"]')))
login.click()

# Wait for the username input to be visible and enter the username
userName = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="text"]')))
userName.send_keys("Username")


# Wait for the next button to be clickable and click it
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//div[@role="group"])[2]//button[2]')))
next_button.click()

# Wait for the password input to be visible and enter the password
password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
password.send_keys("Password")

# Wait for the login button to be clickable and click it
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="LoginForm_Footer_Container"]//div//button')))
login_button.click()

# Function to extract the username and text from a tweet element
def get_tweet(el):
    try:
        userName = el.find_element(By.XPATH, './/span[contains(text(),"@")]').text
        text = el.find_element(By.XPATH, './/div[@lang]').text
        tweets_data = [userName, text]
    except:
        tweets_data = ["userName", "text"]
    return tweets_data

# Lists to store usernames and tweet texts
user_data = []
text_data = []
# Set to track unique tweets to avoid duplicates
tweets_id = set()

scrolling = True

# Scroll through the page and collect tweets 
while scrolling:
    # Find all tweet elements on the page
    tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]')))

    # Process each tweet element
    for tweet in tweets:
        tweet_list = get_tweet(tweet)
        tweet_id = " ".join(tweet_list)
        if tweet_id not in tweets_id:
            tweets_id.add(tweet_id)
            user_data.append(tweet_list[0])
            text_data.append(" ".join(tweet_list[1].split()))

    # Get the current scroll height
    height = driver.execute_script("return document.body.scrollHeight;")
    while True:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait until the new height is greater than the old height
        time.sleep(4)
        new_height = driver.execute_script("return document.body.scrollHeight;")
        
        # To scroll the page until its end
        if new_height == height:
            scrolling = False
            break
        else:
            height = new_height
            break
        
    # To scroll the page until a certain number of tweets is achieved
        # if len(user_data) > 60:
        #     scrolling = False
        #     break
        # else:
        #     height = new_height
        #     break

# Close the driver
driver.quit()

# Create a DataFrame from the collected data
df_tweets = pd.DataFrame(
    {"User": user_data, 
     "Tweet": text_data
     })

# Save the DataFrame to a CSV file
df_tweets.to_csv(r"C:\Users\Hannan Poonawala\OneDrive\Desktop\AMAAN\WebScrape\PROJECTS\TWITTER\tweets-all.csv", index=False)

# Print the DataFrame
print(df_tweets)

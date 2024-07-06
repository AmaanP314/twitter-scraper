# Twitter Tweets Scraper

This project is a Twitter tweets scraper built using Selenium and Python. The scraper logs into Twitter, navigates through tweets, and extracts usernames and tweet texts. The collected data is saved into a CSV file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/amaanp314/twitter-tweets-scraper.git
    cd twitter-tweets-scraper
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download the appropriate ChromeDriver for your version of Chrome:**

    - [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads)

5. **Update the script with your ChromeDriver path and desired user agent.**

## Usage

1. **Update the `path` variable in the script with the path to your ChromeDriver executable:**

    ```python
    path = r"your chromedriver file path\chromedriver.exe"
    ```

2. **Update the `user_agent` variable with your desired user agent:**

    ```python
    user_agent = "your desired user agent"
    ```

3. **Run the script:**

    ```bash
    python twitter_scraper.py
    ```

4. **The script will log into Twitter, scroll through tweets, and save the collected data into a `tweets.csv` file.**

## Project Structure

    twitter-tweets-scraper/
    │
    ├── twitter_scraper.py # Main script to run the scraper
    ├── requirements.txt # Python dependencies
    ├── tweets.csv # Output file with collected tweets data
    └── README.md # Project documentation


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

Amaan Poonawala - [GitHub](https://github.com/amaanp314)

Feel free to reach out for any questions or feedback.



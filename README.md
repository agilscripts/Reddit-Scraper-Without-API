# Reddit-Scraper-Without-API
This Python script allows you to scrape data from the Reddit website using the JSON feed from a subreddit. The script extracts information such as the post title, author, upvotes, and URL. The extracted data is then saved into a CSV file for easy analysis and review.

#### Features

- **Automated Data Extraction**: The script automatically fetches the latest "hot" posts from Reddit.
- **JSON Parsing**: Utilizes Reddit's JSON feed to extract structured data, avoiding the need for HTML parsing.
- **CSV Export**: Saves the scraped data into a CSV file, making it easy to use for further analysis or reporting.
- **No Reddit API Required**: This script does not require the use of Reddit's official API, making it easier to set up and use.

#### How to Use

1. **Install Requirements**: Make sure you have Python installed and the `requests` library. You can install the required library using pip:

   ```bash
   pip install requests
   ```

2. **Run the Script**: Execute the script in your Python environment to scrape the data from Reddit:

   ```bash
   python reddit_scraper.py
   ```

3. **Check the CSV Output**: After running the script, you'll find a `reddit_posts.csv` file in the same directory containing the scraped data.

#### Notes

- **Respect Reddit's Usage Policy**: Even though this script does not use the Reddit API, it's important to respect Reddit's [Terms of Service](https://www.redditinc.com/policies/data-api-terms) and rate limits when scraping data.
- **Customizable**: You can modify the script to scrape different subreddits or extract different types of data as needed.

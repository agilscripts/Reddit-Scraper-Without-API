# Reddit-Scraper-Without-API

This Python script allows you to scrape data from Reddit using the JSON feed from any subreddit. The script extracts information such as post titles, authors, upvotes, and URLs. The extracted data is then saved into a CSV file for easy analysis and review.

#### Features

- **Automated Data Extraction**: Automatically fetches the latest "hot" posts from Reddit.
- **JSON Parsing**: Utilizes Reddit's JSON feed to extract structured data, avoiding the need for HTML parsing.
- **CSV Export**: Saves the scraped data into a CSV file, making it easy to use for further analysis or reporting.
- **No Reddit API Required**: This script does not require the use of Reddit's official API, making it easier to set up and use.
- **Customizable URL**: Easily modify the script to scrape different subreddits by adding `.json` to the end of any subreddit URL and pasting it into the script.

#### How to Use

1. **Install Requirements**: Ensure you have Python installed and the `requests` library. You can install the required library using pip:

   ```bash
   pip install requests
   ```

2. **Customize the Subreddit URL**: To scrape data from a different subreddit, simply add `.json` to the end of the subreddit URL you wish to scrape. For example, to scrape the "hot" posts from the `/r/python` subreddit, use `https://www.reddit.com/r/python/hot/.json`. Copy and paste the modified URL into the script where it specifies the subreddit URL.

3. **Run the Script**: Execute the script in your Python environment to scrape data from Reddit:

   ```bash
   python reddit_scraper.py
   ```

4. **Check the CSV Output**: After running the script, you'll find a `reddit_posts.csv` file in the same directory containing the scraped data.

#### Notes

- **Respect Reddit's Usage Policy**: Even though this script does not use the Reddit API, it's important to respect Reddit's [Terms of Service](https://www.redditinc.com/policies/data-api-terms) and rate limits when scraping data.
- **Highly Customizable**: You can modify the script to scrape different subreddits or extract different types of data by adjusting the URL and data extraction logic as needed.

import requests
import csv

# Step 1: Fetch the JSON data from the Reddit API
url = "https://www.reddit.com/r/learnprogramming/hot/.json"
headers = {'User-agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Step 2: Parse the JSON response
    reddit_data = response.json()
    posts = reddit_data['data']['children']

    # Step 3: Prepare to write data to CSV
    with open('reddit_posts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Title', 'Author', 'Upvotes', 'URL'])

        # Step 4: Extract and write the data for each post
        for post in posts:
            post_data = post['data']
            title = post_data['title']
            author = post_data['author']
            upvotes = post_data['ups']
            post_url = 'https://www.reddit.com' + post_data['permalink']
            writer.writerow([title, author, upvotes, post_url])

    print("Data has been successfully written to reddit_posts.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

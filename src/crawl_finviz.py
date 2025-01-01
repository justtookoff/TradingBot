import requests
from bs4 import BeautifulSoup
import time
import urllib.request
import os
from datetime import datetime
import re

URL = "https://finviz.com/news.ashx"
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}


def sanitize_dir_name(name):
    # Define prohibited characters for directory names
    prohibited_chars = r'[<>:"/\\|?*]'
    # Replace prohibited characters with an underscore
    sanitized_name = re.sub(prohibited_chars, '_', name)
    return sanitized_name

def crawl_url_finviz(url):
    """Crawls a given URL and extracts links."""
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract links
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

    except requests.exceptions.RequestException as e:
        print(f"Error crawling {url}: {e}")
        return []
    

def fetch_article(url):
    try:
        # Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None, None

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # print('soup:', soup)

    # Extract the title - this example assumes the title is within the <title> tag
    # or a <h1> tag, but this may vary based on the website's structure
    title = soup.title.string if soup.title else None
    if not title:
        title_tag = soup.find('h1')
        title = title_tag.get_text() if title_tag else "No title found"

    # Extract the body - this example assumes article content is within <p> tags
    # Alternatively, a more specific selector or class may be needed
    body_parts = soup.find_all('p')
    body = '\n'.join(part.get_text() for part in body_parts)

    return title, body


if __name__ == "__main__":
    base_url = "https://finviz.com/news.ashx?v=3"
    links = crawl_url_finviz(base_url)
    article_dir = "./../articles/" + datetime.now().strftime("%y%m%d_%H%M%S") + "/"

    # Check if the directory exists, and create it if not
    if not os.path.exists(article_dir):
        os.makedirs(article_dir)
        print(f"Directory '{datetime.now().strftime("%y%m%d_%H%M%S")}' created.")
    else:
        print(f"Directory '{datetime.now().strftime("%y%m%d_%H%M%S")}' already exists.")

    for link in links:
        if link.startswith('https://'):
            print(link)
            article_url = link
        elif link.startswith('quote'):
            ticker = link.split('=')[1]
            article = requests.get(article_url)
            soup = BeautifulSoup(article.content, 'html5lib')
            # print(article)

            article_title, article_body = fetch_article(article_url)
            if article_title is None:
                continue
            article_title_ = ticker + '_' + sanitize_dir_name(article_title.replace(' ', '_'))
            print('title:', article_title_)
            with open(article_dir + '/' + article_title_ + '.txt', 'w') as f:
                f.write(article_body)

            # break

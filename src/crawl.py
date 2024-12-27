import requests
from bs4 import BeautifulSoup

URL = "https://finviz.com/news.ashx"
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}


def crawl(url):
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

if __name__ == "__main__":
    start_url = "https://finviz.com/news.ashx?v=3"
    links = crawl(start_url)

    for link in links:
        if link.startswith('https://'):
            print(end='\n')
            print(link, end=' ')
        elif link.startswith('quote'):
            print(link.split('=')[1], end=' ')

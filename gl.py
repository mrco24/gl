import requests
from bs4 import BeautifulSoup
import argparse
import urllib.parse

banner = '''
...
'''

blacklist = ['support.google.com', 'accounts.google.com']

print(banner)

parser = argparse.ArgumentParser(description='Google Dork Scraper')
parser.add_argument('-d', '--dork', help='Specify the Google dork', required=True)
args = parser.parse_args()

dorks = args.dork
mainurl = f"https://www.google.com/search?q={urllib.parse.quote(dorks)}&start="

def single_scrap(url):
    urls = []
    try:
        request = requests.get(url).text
        soup = BeautifulSoup(request, 'html.parser')
        links = soup.select('a[href^="/url?q="]')
        for link in links:
            gg = link['href'].replace("/url?q=", "").split('&sa=')[0]
            hk = urllib.parse.unquote(gg)
            gf = hk.split("//")[1]
            k = gf.split("/")[0]
            if k not in blacklist:
                urls.append(hk)
    except Exception as e:
        print(f"Error: {e}")
    return urls

page = 0
while True:
    result_urls = single_scrap(mainurl + str(page))
    if not result_urls:
        break
    for url in result_urls:
        print(url)
    page += 10

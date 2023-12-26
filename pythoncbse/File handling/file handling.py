
# working on web scraping
import requests
import bs4
url='https://books.toscrape.com/catalogue/page-2.html'
soup=requests.get(url)
contents=bs4.BeautifulSoup(soup.content)
# print(contents)

example=contents.select('.product_pod')
# print(example)
for x in example['star-rating Two']:
    print(x.text)
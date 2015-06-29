import requests
from urllib import quote
from bs4 import BeautifulSoup

SEARCH_URL = 'http://www.crunchyroll.com/search?q=%s'
RESULT_ID  = 'aux_results'

def search(query):
  # Encode the query
  query = quote(query.replace(' ', '+'))

  # Request the url
  r = requests.get(SEARCH_URL % query)
  return r.text

def parse(body):
  soup = BeautifulSoup(body)

  # Return the url of the first result
  return soup.find(id=RESULT_ID).a['href']

def main():
  query = raw_input()
  body = search(query)
  url = parse(body)
  print(url)

if __name__ == '__main__':
  main()


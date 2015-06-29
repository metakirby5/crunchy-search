import requests
from urllib import quote
from bs4 import BeautifulSoup

SEARCH_URL = 'http://www.crunchyroll.com/search?q=%s'
RESULT_ID  = 'aux_results'

class SearchError(Exception):
  pass

def search(query):
  """
  Returns the first result of a Crunchyroll search
  as a dict with keys of:

  {
    'url': str,
    'series': str,
    'ep_name': str,
    'ep_no': int
  }

  Raises SearchError if no results found.
  """
  # Request the url
  try:
    r = requests.get(SEARCH_URL % quote(query))
  except requests.exceptions.ConnectionError:
    raise SearchError('No connection')

  soup = BeautifulSoup(r.text)

  # Return the first result
  try:
    result = soup.find(id=RESULT_ID).a
    return {
      'url':      result['href'],
      'series':   result.find(class_='series').string,
      'ep_name':  result.find(class_='name').string,
      'ep_no':    int(result.find(class_='ordernum').string.split()[-1]),
    }
  except TypeError:
    raise SearchError('No results found')

def main():
  query = raw_input()
  result = search(query)
  print(result['url'])

if __name__ == '__main__':
  main()


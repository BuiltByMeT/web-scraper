from bs4 import BeautifulSoup
import requests
# requests allows python to send HTTP requests

# ADJUST: add url to scrape
url = '[url]'

# maybe make parser BeautifulSoup(,'[parser]') something different (universal?)
req = requests.get(url)
soup = BeautifulSoup(req.text,'lxml')

# ADJUST: add in class/id to find
class_to_find = '[class name]'
id_to_find = '[id name]'

# ADJUST: remove uneccessary call
class_found = soup.find_all(class_to_find)
id_found = soup.find(id = id_to_find)

# ADJUST: remove/alter as necessary
# if looking for just a piece of content nested
# but w/o class/id/etc add their tags
# ex. id_found.[p].[span].[etc]
nested_content = id_found.p.span

# ADJUST: remove uneccessary calls
contents_found = class_found.contents
contents_found = id_found.get_text()
contents_found = nested_content.get_text()
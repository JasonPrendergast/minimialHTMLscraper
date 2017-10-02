from lxml import html
import requests

page = requests.get('https://www.jobsinkent.com/search.html?p=2')
tree = html.fromstring(page.content)
url=tree.xpath('//h3/a/@href')
print(url)


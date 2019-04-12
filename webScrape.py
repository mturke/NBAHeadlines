from lxml import html
import requests
response = requests.get('http://www.espn.com/nba/')
doc = html.fromstring(response.text)
title1 = doc.cssselect('div.contentItem__header__headings')[0].text_content()
title2 = doc.cssselect('ul.headlineStack__list')[0].text_content()
title3 = doc.cssselect('div.headlineStack')[0].text_content()

print()
print("The top headlines on the ESPN NBA homepage:")
print()
print(title1, end= '\t')
print()
#print(title2)
print()
print(title3, end = '\t')
print()




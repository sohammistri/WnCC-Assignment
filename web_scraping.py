import requests,sys,bs4

res=requests.get('https://gadgets.ndtv.com/news')	#request to a tech news website

try:					#try block to check if news site is valid or not
    res.raise_for_status()
except Exception as exc:	#exception block to avoid abnormal termination
    print('There was a problem: %s' % (exc))
    sys.exit()

#print(res.text[:500])

news_soup=bs4.BeautifulSoup(res.text,"html.parser")	#beautiful soup for web sacraping

for elements in news_soup.find_all('span','news_listing'):	#it was seen that headlines have a common html feature div class='news_listing' and hence this parsing
	print(elements.getText())		#printing headlines


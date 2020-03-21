from newsapi import NewsApiClient #importing newsAPI

newsapi=NewsApiClient(api_key='39070fd0c030420bb046102d48c0d0ee')

data=newsapi.get_everything(domains='techcrunch.com',language='en')	#getting top headlines from the techcrunch.com site

for value in data['articles']:	#data is a dict, data['articles'] is a list containing the info
	print(value['title'])		#Only the title i.e the headlines

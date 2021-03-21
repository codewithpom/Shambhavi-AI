import requests
import os
obj = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3ba9062408ff4b529ac50909a5f77959')
i = -1
articles = obj.json()['articles']
for i in range(0,len(articles)-1):
    i = i+1
    file = open('news.html','a')
    title = articles[i]['title']
    image_url = articles[i]['urlToImage']
    print(image_url)
    print(title)
    file.write('<h1>'+title+'</h1> <br><br>')
    file.close()
    file = open('news.html', 'a')
    file.write('<img src="'+image_url+'"/>')
    file.close()
    print(i)




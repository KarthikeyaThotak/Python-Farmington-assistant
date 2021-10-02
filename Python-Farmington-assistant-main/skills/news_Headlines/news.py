import requests
import json

# print(data['value'][::4]['title'])

class News:
    def __init__(self):
        self.url = "https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey=dea33cf20981497abaf3e960c82c5b14"
        #self.url  = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/TrendingNewsAPI"
        self.querystring = {"pageNumber":"1","pageSize":"5","withThumbnails":"false","location":"us"}
        self.header = {
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
            'x-rapidapi-key': "c165bfa4b4msh6f07170f5c719fep18e2e0jsn6c0524e66b81"}
        self.response = requests.request("GET", self.url)#, headers=self.header, params=self.querystring)

    def news(self):
        paper = []
        data = json.loads(self.response.text)
        for i in range(0,9):
            headlines = data['articles'][i]['title']
            paper.append(headlines)
        return paper


News = News()

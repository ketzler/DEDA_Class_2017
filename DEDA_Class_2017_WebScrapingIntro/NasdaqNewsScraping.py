import requests
from bs4 import BeautifulSoup as soup
import datetime
import pandas as pd
import os

# Using the requests module to get source code from the url
nasdaq_url = 'http://www.nasdaq.com/news/market-headlines.aspx'
url_request = requests.get(nasdaq_url)
url_content = url_request.content
# Using BeautifulSoup to parse webpage source code
parsed_content = soup(url_content)
# Finding all the <p> tag content
containers = parsed_content.find_all('p')

# initial empty list to load the data
link_list = []
title_list = []
time_list = []
tag_list = []

for container in containers:
    # Using .find_all() method to search tag name and attribute
    container_a = container.find_all('a', {"id":"two_column_main_content_la1_rptArticles_hlArticleLink_0"})
    for item in container_a:
        # Loop in the <a> tag
        news_link = item.get('href').strip()  # strip() method can remove specific chars at the head and tail
        news_title = item.text.strip()
        link_list.append(news_link)
        title_list.append(news_title)
    container_span = container.find_all('span', {'class': 'small'})
    for item in container_span:
        item_split = item.text.split(' - ')
        print(item_split)
        time = datetime.datetime.strptime(item_split[0], '%m/%d/%Y %I:%M:%S %p')
        # Formatting date see further more: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        time_list.append(time)
        # Using try...except to catch unexpected condition so that program can keep running
        try:
            tag = item_split[1].split('  in ')[1].strip()
        except Exception:
        # If the tag doesn't exist, mark it as an empty list
            tag = []
        tag_list.append(tag)
nasdaq_info = zip(title_list, time_list, link_list, tag_list)
nasdaq_info_df = pd.DataFrame(list(nasdaq_info), columns=['title', 'time', 'link', 'tag'])
nasdaq_info_df.to_csv(os.getcwd() + '/DEDA_Class_2017_WebScrapingIntro/Nasdaq_News.csv')


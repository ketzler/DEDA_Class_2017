
[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **Digital Economy and Decision Analytics** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : DEDA_Class_2017_WebScraping
Published in : Digital Economy and Decision Analytics
Description : Demonstrate how to scrape different type of web pages in Python
Keywords :
- Python
- Teaching
- Web Data
- RSS
- Json
- XML
Author : Cathy YH Chen, Junjie Hu

```

### Python Code:
```python

import feedparser

content = feedparser.parse("https://www.ft.com/?edition=international&format=rss")

contentWSJ = feedparser.parse("http://www.wsj.com/public/page/rss_news_and_feeds.html")

#list all titles
print("\nTitles-------------------------\n")
for index, item in enumerate(content.entries):
    print("{0}.{1}".format(index, item["title"]))


#list all description
print("\r\nDescriptions-------------------\r\n")
for index, item in enumerate(content.entries):
    print("{0}.{1}\n".format(index, item["description"]))


```




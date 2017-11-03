import feedparser

# retrieve RSS feedback
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

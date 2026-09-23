import feedparser

rss = "https://news.google.com/rss/search?q=new+cafe+finland"

feed = feedparser.parse(rss)

for entry in feed.entries:
    print(entry.title)
    print(entry.link)
    print("-" * 50)

import feedparser
import csv

rss = "https://news.google.com/rss/search?q=new+cafe+finland"

feed = feedparser.parse(rss)

with open("leads.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["Title", "Link"])

    for entry in feed.entries:
        writer.writerow([
            entry.title,
            entry.link
        ])

print("CSV file created.")

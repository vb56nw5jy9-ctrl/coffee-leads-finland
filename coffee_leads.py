import feedparser
import csv

feeds = {
    "New Cafes":
        "https://news.google.com/rss/search?q=new+cafe+finland",

    "New Restaurants":
        "https://news.google.com/rss/search?q=new+restaurant+finland",

    "Hotel Renovations":
        "https://news.google.com/rss/search?q=hotel+renovation+finland",

    "Barista Jobs":
        "https://news.google.com/rss/search?q=barista+finland"
}

with open("leads.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Category",
        "Title",
        "Link"
    ])

    for category, rss_url in feeds.items():

        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            writer.writerow([
                category,
                entry.title,
                entry.link
            ])

print("Coffee leads created.")


import requests
from csv import writer
from bs4 import BeautifulSoup

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
all_articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in all_articles:
        anchor_tag = article.find("a")
        time_tag = article.find("time")

        title = anchor_tag.get_text()
        link = anchor_tag["href"]
        date = time_tag["datetime"]

        csv_writer.writerow([title, link, date])

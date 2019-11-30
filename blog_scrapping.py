import requests
from bs4 import BeautifulSoup
from csv import writer

all_blogs_scrapped = []

base_url = "https://www.rithmschool.com"
page_url = "/blog?page=1"

while page_url:
    res = requests.get(f"{base_url}{page_url}")
    soup = BeautifulSoup(res.text, "html.parser")
    all_blogs = soup.find_all("article")

    for blog in all_blogs:
        anchor_tag = blog.find("a")
        time_tag = blog.find("time")

        blog_date = time_tag["datetime"]
        blog_title = anchor_tag.get_text()
        blog_slug = anchor_tag["href"]
        blog_link = f"{base_url}{blog_slug}"

        all_blogs_scrapped.append({
            "blog_date": blog_date,
            "blog_title": blog_title,
            "blog_link": blog_link,
        })

    pagination_container = soup.find(attrs={"class": "pagination"})
    next_button = pagination_container.find(attrs={"class": "next"})
    page_url = next_button.find("a")["href"] if next_button else None

with open("all_blogs_scrapped.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["blog_date", "blog_title", "blog_link"])

    for single_blog_scrapped in all_blogs_scrapped:
        blog_date = single_blog_scrapped["blog_date"]
        blog_title = single_blog_scrapped["blog_title"]
        blog_link = single_blog_scrapped["blog_link"]
        csv_writer.writerow([blog_date, blog_title, blog_link])

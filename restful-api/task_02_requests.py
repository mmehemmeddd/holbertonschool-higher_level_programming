#!/usr/bin/python3
"""i send api with requests"""
print(response.status_code)
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post["title"])
    else:
        print("Request failed")


def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        # CSV üçün struktur hazırlamaq
        posts = []
        for post in data:
            posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        # CSV yazmaq
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
    else:
        print("Request failed")


# Test
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()

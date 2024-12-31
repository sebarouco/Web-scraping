import requests

url = "https://www.google.com/"
response = requests.get(url)

if response.status_code == 200:
    print("Page fetched successfully!")
    print(response.text)  # Print the HTML content
else:
    print("Failed to fetch the page.")

from bs4 import BeautifulSoup

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

# Extract the title of the page
title = soup.title.text
print("Page Title:", title)

# Find all the links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
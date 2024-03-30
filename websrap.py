import requests
from bs4 import BeautifulSoup
import json

with open("product.txt","r") as file:
    search_terms = file.readlines()

results = []

for search_term in search_terms:
    search_term = search_term.strip().lower()
    # URL of the website to scrape
    url = f"https://boycott.thewitness.news/target/{search_term}"

    # Send a GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    if response.status_code == 200:
        product_name = soup.find("p", class_="mantine-focus-auto m-b6d8b162 mantine-Text-root").text.strip()
        if search_term.lower() == product_name.lower():
            about_product = soup.find("div", class_="m-4081bf90 mantine-Group-root").text.strip()
            why_boycott = soup.find("div", class_="m-599a2148 mantine-Card-section Listing_section__Pz_36").text.strip()
            more = soup.find("span", class_="mantine-focus-auto m-b6d8b162 mantine-Text-root").text.strip()


            boycott = True # continue your logic here

            result = {
                "product_name": product_name,
                "boycott": boycott,
                "about": about_product,
                "why_boycott": why_boycott,
                "more": more
            }
            results.append(result)


    elif response.status_code == 404:       
        boycott = False 
        result = {
                "product_name": search_term.title(),
                "boycott": boycott,
                "about": "",
                "why_boycott": "",
                "more": ""
        }

        results.append(result)

with open("data.json", "w") as file:
    json.dump(results, file, indent=4)


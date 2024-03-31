import requests
from bs4 import BeautifulSoup
import json

with open("product.txt","r") as file:
    search_terms = file.readlines()

results = []

for search_term in search_terms:
    search_term = search_term.strip()
    # URL of the website to scrape
    url = f"https://boycott.thewitness.news/target/{search_term}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the relevant content within the HTML based on class name
    # alert_div = soup.find("div", class_="m-a5d60502 mantine-Alert-wrapper")
    try: 
        product_name = soup.find("p", class_="mantine-focus-auto m-b6d8b162 mantine-Text-root").text.strip()

        if search_term.title() == product_name:
            about_product = soup.find("div", class_="m-4081bf90 mantine-Group-root").text.strip()
            why_boycott = soup.find("div", class_="m-599a2148 mantine-Card-section Listing_section__Pz_36").text.strip()
            more = soup.find("span", class_="mantine-focus-auto m-b6d8b162 mantine-Text-root").text.strip()
            # print("about_product\n",about_product)
            # print("why_boycott\n",why_boycott)
            # print("more\n",more)

            boycott = True # continue your logic here

            result = {
                "product_name": product_name,
                "boycott": boycott,
                "why_boycott": why_boycott,
                "more": more
            }


    except AttributeError:
        # Apply more logic here
        boycott = False #Continue your logic here

        result = {
                "product_name": search_term.title(),
                "boycott": boycott,
                "why_boycott": "",
                "more": ""
        }
    results.append(result)

with open("data.json", "w") as file:
    json.dump(results, file, indent=4)


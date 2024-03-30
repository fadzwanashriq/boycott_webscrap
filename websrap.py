import requests
from bs4 import BeautifulSoup

# Get user input for the search term
search_term = input("Enter the search term: ")

# URL of the website to scrape
url = f"https://boycott.thewitness.news/search/{search_term}"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant content within the HTML based on class name
alert_div = soup.find("div", class_="m-a5d60502 mantine-Alert-wrapper")

# Check if the alert_div exists
if alert_div:
    # Extract the text content of the alert_div
    result_message = alert_div.text.strip()

    # Check if the specified string is present in the result message
    if "We were unable to find anything for that search." in result_message:
        print("not boycott")
    else:
        print("boycott")
else:
    print("boycott")
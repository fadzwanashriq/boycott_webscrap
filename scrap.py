from time import sleep
import requests 
from bs4 import BeautifulSoup
import json

import sqlite3

def createTable():
    conn = sqlite3.connect("boycott.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS boycotts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        boycott BOOLEAN,
        about TEXT,
        why_boycott TEXT,
        more_info TEXT,
        alternative TEXT
    )""")
    conn.commit()
    conn.close()

def insertData(product_name, boycott, about, why_boycott, more_info, alternative):
    conn = sqlite3.connect("boycott.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO boycotts (product_name, boycott, about, why_boycott, more_info, alternative) VALUES (?,?,?,?,?,?)",(product_name, boycott, about, why_boycott, more_info, alternative))
    conn.commit()
    conn.close()

def prettyPrint(results:list[any]):
    for result in results:
        print(f"Product Name: {result[0]}")
        print(f"Boycott: {result[1]}")
        print(f"About: {result[2]}")
        print(f"Why Boycott: {result[3]}")
        print(f"More Info: {result[4]}")
        print("")

#structure of json file
#
# {
#     "pageProps": {
#         "listing": {
#             "_id": "65679f0ffac1794dbaea5019",
#             "id": "7up",
#             "logo": "https://assets.turbologo.com/blog/en/2020/02/19084627/7up-cover.jpg",
#             "name": "7up",
#             "source": "https://www.bloomberg.com/view/articles/2018-08-22/pepsico-s-sodastream-purchase-is-sweet-news-for-israelis?leadSource=uverify%20wall",
#             "description": "Soft drink, a distributed internationally by PepsiCo",
#             "reason": "The international distributer of 7up, PepsiCo, bought SodaStream for $3.2bn and owns 50% of Sabra both of which had taken advantage of the Israeli occupation of Palestine.",
#             "category": [
#                 "drinks"
#             ],
#             "howToBoycott": [
#                 "Don't buy 7up products.",
#                 "Don't sell 7up products",
#                 "Don't work for the PepsiCo Company"
#             ],
#             "alternatives": [
#                 "Supermarket own brand products, eg. Morrisons",
#                 "Barr Drinks (owner of Irn Bru)"
#             ]
#         }
#     },
#     "__N_SSG": true
# }
        
def process_json(site_json):
    boycott = True
    product_name = site_json["pageProps"]["listing"]["name"]
    about = site_json["pageProps"]["listing"]["description"]
    why_boycott = site_json["pageProps"]["listing"]["reason"]
    more_info = site_json["pageProps"]["listing"]["source"]
    alternative = ""

    insertData(product_name, boycott, about, why_boycott, more_info, alternative)

def select_all():
    conn = sqlite3.connect("boycott.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM boycotts")
    results = cursor.fetchall()
    conn.close()
    return results

# createTable()

with open("product.txt","r") as file:
    search_terms = file.readlines()
    #SELECT 5 search terms
    search_terms = search_terms[5:]
    for search_term in search_terms:
        search_term = search_term.strip().lower()

        url = f"https://boycott.thewitness.news/_next/data/ukcz58q3IRxINhzxONStx/target/{search_term}.json?id={search_term}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        site_json =  json.loads(soup.text)

       
        sleep(5)
        process_json(site_json)
# #benchmarking timing
# import time
# start = time.time()
# print("Start time: ", start)
# prettyPrint(select_all())
# end = time.time()
# print("End time: ", end)
# print("Time taken: ", end - start)

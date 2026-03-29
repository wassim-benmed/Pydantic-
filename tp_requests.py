# ============================================
# TP : Python Requests & Web Scraping
# Nom : Wassim Ben Med
# ============================================

import requests
from bs4 import BeautifulSoup
import urllib3

# Désactiver les warnings SSL pour les tests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ----------- 1. GET Request -----------
print("=== GET Request ===")

url_get = "https://httpbin.org/get"  # site fiable pour GET request
response_get = requests.get(url_get, verify=False)

print("Status Code:", response_get.status_code)


# ----------- 2. Request Content -----------
print("\n=== Response Content ===")
print(response_get.content[:200])  # afficher seulement une partie du contenu


# ----------- 3. POST Request -----------
print("\n=== POST Request ===")

data = {"name": "Salah", "message": "Hello!"}
url_post = "https://httpbin.org/post"

response_post = requests.post(url_post, json=data, verify=False)

print("POST Status:", response_post.status_code)

response_data = response_post.json()
print("Response JSON:", response_data["json"])


# ----------- 4. Handling Errors -----------
print("\n=== Handling Errors ===")

response_error = requests.get("https://httpbin.org/status/404", verify=False)

if response_error.status_code != 200:
    print(f"HTTP Error: {response_error.status_code}")


# ----------- 5. Timeout -----------
print("\n=== Timeout Example ===")

try:
    response_timeout = requests.get("https://httpbin.org/delay/10", timeout=5, verify=False)
except requests.exceptions.Timeout:
    print("Request timed out!")


# ----------- 6. Headers -----------
print("\n=== Headers Example ===")

headers = {
    "Authorization": "Bearer TEST_TOKEN"
}

response_headers = requests.get("https://httpbin.org/headers", headers=headers, verify=False)

print("Headers Response:", response_headers.json())


# ----------- 7. Web Scraping -----------
print("\n=== Web Scraping ===")

# Pour le scraping, on peut utiliser une page test simple d'HTTPBin
url_scrape = "https://httpbin.org/html"
response_scrape = requests.get(url_scrape, verify=False)

soup = BeautifulSoup(response_scrape.content, "html.parser")

# Title
title = soup.title.text if soup.title else "No title found"

# First paragraph
p_tag = soup.find("p")
content = p_tag.text if p_tag else "No paragraph found"

# Links
links = [a["href"] for a in soup.find_all("a") if a.get("href")]

print("Title:", title)
print("Content:", content)
print("Links:", links)


# ----------- 8. Fin -----------
print("\n=== Fin du TP ===")
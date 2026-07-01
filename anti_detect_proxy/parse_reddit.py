import requests
import re
import urllib.parse
from bs4 import BeautifulSoup

PROXY_URL = "http://localhost:8815/api/v1/scrape"

def fetch(url):
    return requests.post(PROXY_URL, json={
        "url": url,
        "method": "GET",
        "impersonate": "chrome120",
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.reddit.com/"
        }
    }).json()

data = fetch("https://www.reddit.com/r/python/")
html = data.get("text", "")

if "Reddit - Please wait for verification" in html:
    print("Encountered JS challenge. Solving...")
    soup = BeautifulSoup(html, "html.parser")
    form = soup.find("form")
    action = form.get("action", "/r/python/")
    
    # Extract hidden inputs
    params = {}
    for inp in form.find_all("input", type="hidden"):
        params[inp.get("name")] = inp.get("value", "")
        
    # Extract the JS challenge string
    # e.g. await(async e=>e+e)("4d131b027420c3e8")
    match = re.search(r'await\(async e=>e\+e\)\("([a-f0-9]+)"\)', html)
    if match:
        token_str = match.group(1)
        solution = token_str + token_str
        params["solution"] = solution
    
    # Submit the form
    submit_url = "https://www.reddit.com" + action + "?" + urllib.parse.urlencode(params)
    print("Submitting to:", submit_url)
    
    data = fetch(submit_url)
    html = data.get("text", "")
    
    print("New HTML length:", len(html))
    print("Snippet:", html[:200])


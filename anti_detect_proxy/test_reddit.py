import requests

PROXY_URL = "http://localhost:8815/api/v1/scrape"

def test_url(url):
    print(f"Testing {url}")
    resp = requests.post(PROXY_URL, json={
        "url": url,
        "method": "GET",
        "impersonate": "chrome120",
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9"
        }
    })
    try:
        data = resp.json()
        print("Status:", data.get("status_code"))
        text = data.get("text", "")
        print("Text preview:", text[:200])
    except Exception as e:
        print("Failed:", e, resp.text)

test_url("https://old.reddit.com/r/python.json")
test_url("https://www.reddit.com/r/python/")

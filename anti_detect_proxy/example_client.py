import json
import requests

# Địa chỉ của Proxy API bạn vừa dựng (đang chạy ở port 8815)
PROXY_API_URL = "http://localhost:8815/api/v1/scrape"

def scrape_cloudflare_site(url: str, impersonate: str = "chrome120"):
    """
    Hàm này gửi yêu cầu cào dữ liệu tới Proxy API của bạn.
    Proxy API sẽ dùng curl_cffi giả mạo trình duyệt để vượt Cloudflare.
    """
    payload = {
        "url": url,
        "method": "GET",
        # Bạn có thể chọn loại trình duyệt giả mạo, ví dụ: chrome120, safari17_0...
        "impersonate": impersonate,
        # Nếu muốn cào Reddit, nên thêm các header cơ bản này để giống người dùng thật hơn
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }
    }

    print(f"Đang gửi request cào dữ liệu từ: {url}...")
    
    # Gửi request tới hệ thống Proxy API của bạn
    response = requests.post(PROXY_API_URL, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Thành công vượt bảo mật!")
        print(f"Mã trạng thái trả về từ trang gốc: {data['status_code']}")
        
        # In ra 500 ký tự đầu tiên của nội dung lấy được
        html_content = data.get("text", "")
        print(f"Nội dung thu được ({len(html_content)} bytes):")
        print(html_content[:500] + "...\n")
        
        return html_content
    else:
        print("❌ Lỗi khi gọi Proxy API:")
        print(response.text)
        return None

if __name__ == "__main__":
    # Ví dụ 1: Thử trích xuất một trang kiểm tra Cloudflare
    test_cf_url = "https://nowsecure.nl" # Trang web này luôn bật Cloudflare bot protection
    scrape_cloudflare_site(test_cf_url, impersonate="chrome120")
    
    print("-" * 50)
    
    # Ví dụ 2: Thử trích xuất Reddit (Reddit chặn bot rất gắt)
    reddit_url = "https://www.reddit.com/r/python/top/?t=day"
    # Lấy luôn file JSON nội dung của reddit (thêm .json vào cuối url)
    reddit_json_url = "https://www.reddit.com/r/python/top.json?t=day" 
    scrape_cloudflare_site(reddit_json_url, impersonate="safari17_0")

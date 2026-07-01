<div align="center">
  <h1>👻 PhantomScrape Lite</h1>
  <p><strong>A Lightweight, Open-Source Web Scraping API with Basic TLS Spoofing</strong></p>
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
</div>

---

## 📖 Introduction
PhantomScrape Lite is a fast, easy-to-deploy API built on FastAPI. It uses `curl_cffi` to provide basic TLS fingerprint spoofing (impersonating Chrome 110), allowing you to scrape websites that have basic bot protection without getting blocked immediately.

This is the **Free, Open-Source** edition of the PhantomScrape ecosystem.

---

## ⚡ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 3. Usage
Send a POST request to `/api/v1/scrape`:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/scrape' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://tls.browserleaks.com/json",
  "method": "GET"
}'
```

Or visit `http://localhost:8000/docs` to use the interactive Swagger UI.

---

## ⚠️ Limitations of Lite Version

While PhantomScrape Lite is great for basic scraping, it **DOES NOT** have advanced bypass capabilities. You **will be blocked** (403 Forbidden, 503 Service Unavailable) by advanced protections like:
- **Cloudflare JS Challenges & Turnstile**
- **Datadome & PerimeterX (advanced configurations)**
- **reCAPTCHA / hCaptcha intercepts**

If you need to bypass these, you need the **Pro Version**.

---

## 🚀 Upgrade to PhantomScrape Pro

Unlock the full power of web scraping with our Pro versions. Stop worrying about getting blocked!

> [!WARNING]
> **Getting 403 or 503 errors on Cloudflare-protected sites?**
> PhantomScrape Lite only does TLS spoofing. To solve complex JS challenges automatically, you need a headless browser solution.
> 👉 **[Get PhantomScrape Pro V1 - The Cloudflare Bypass Master](https://gumroad.com/l/placeholder-v1)**

> [!IMPORTANT]
> **Need the Ultimate All-in-One Solution? ($89)**
> PhantomScrape Pro V2 is an absolute beast for data extraction.
> - 🔥 **Playwright Stealth Browser integration**
> - 🔄 **Auto-Fallback Bypass WAF (Cloudflare/Google)**
> - 🌍 **Auto Free Proxy Rotator**
> - 🧠 **AI-Ready Markdown Parser** (Perfectly extracts content while protecting layout for LLMs)
> 
> 👉 **[Get PhantomScrape Pro V2 Now](https://gumroad.com/l/placeholder-v2)**

---

## 🛠 Project Structure
```text
.
├── app
│   ├── api
│   │   └── endpoints.py   # API routing
│   ├── models
│   │   └── schemas.py     # Pydantic validation
│   ├── services
│   │   └── scraper.py     # curl_cffi logic
│   └── main.py            # FastAPI setup
├── requirements.txt
└── README.md
```

## 📄 License
This "Lite" version is distributed under the **GNU AGPLv3 License**. 

**Điều kiện cơ bản của AGPLv3:**
- Bạn có thể sử dụng miễn phí cho mục đích cá nhân, học tập hoặc dự án mã nguồn mở.
- Nếu bạn sử dụng code này trong một dự án thương mại, hoặc cung cấp nó như một dịch vụ mạng (SaaS), bạn **bắt buộc phải công khai toàn bộ mã nguồn dự án của bạn** dưới cùng giấy phép AGPLv3.

**Bạn muốn sử dụng cho dự án thương mại mã nguồn kín (Closed-Source)?**
Để không bị ràng buộc bởi điều khoản mã nguồn mở trên và có toàn quyền sử dụng, chỉnh sửa cho dự án thương mại của công ty, vui lòng mua giấy phép Thương Mại đi kèm trong bản **PhantomScrape Pro V1 / V2**.

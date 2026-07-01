import asyncio
from curl_cffi import requests
from typing import Dict, Any, Optional

class ScraperService:
    """
    Core scraping service for PhantomScrape Lite.
    Uses curl_cffi for basic TLS spoofing.
    Does NOT include advanced bypass, proxies, or auto-fallback.
    """
    
    @staticmethod
    async def scrape(
        url: str, 
        method: str = "GET", 
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30
    ) -> Dict[str, Any]:
        try:
            # We use asyncio.to_thread since requests in curl_cffi can be blocking
            # curl_cffi does have AsyncSession but to keep it perfectly simple and robust for this Lite version:
            async with requests.AsyncSession(impersonate="chrome110") as session:
                response = await session.request(
                    method=method.upper(),
                    url=url,
                    headers=headers,
                    timeout=timeout,
                    allow_redirects=True
                )
                
                return {
                    "url": str(response.url),
                    "status_code": response.status_code,
                    "content": response.text,
                    "headers": dict(response.headers),
                    "error": None
                }
                
        except requests.errors.RequestsError as e:
            # Return the exact error, no fallback in Lite version
            return {
                "url": url,
                "status_code": 0,
                "content": "",
                "headers": {},
                "error": f"Request failed: {str(e)}"
            }
        except Exception as e:
            return {
                "url": url,
                "status_code": 500,
                "content": "",
                "headers": {},
                "error": f"Internal server error: {str(e)}"
            }

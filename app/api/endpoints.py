from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import ScrapeRequest, ScrapeResponse
from app.services.scraper import ScraperService

router = APIRouter()

@router.post("/scrape", response_model=ScrapeResponse, summary="Scrape a webpage with basic TLS spoofing")
async def scrape_url(request: ScrapeRequest):
    """
    Scrape a target URL using basic TLS fingerprint spoofing (Chrome 110).
    
    **Limitations of Lite Version**: 
    This will NOT bypass Cloudflare JS Challenges, reCAPTCHA, or advanced bot protection.
    If you encounter 403 or 503 errors on protected sites, consider upgrading to PhantomScrape Pro.
    """
    result = await ScraperService.scrape(
        url=str(request.url),
        method=request.method,
        headers=request.headers,
        timeout=request.timeout
    )
    
    if result.get("error"):
        # We still return a 200 OK for the API call itself, but with the error inside the JSON
        # OR we can raise HTTPException. Returning in JSON is often better for scraping APIs
        pass
        
    return ScrapeResponse(**result)

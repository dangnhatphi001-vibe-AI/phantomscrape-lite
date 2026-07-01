from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, Dict

class ScrapeRequest(BaseModel):
    url: HttpUrl = Field(..., description="The target URL to scrape")
    method: str = Field(default="GET", description="HTTP method to use")
    headers: Optional[Dict[str, str]] = Field(default=None, description="Custom headers to send")
    timeout: int = Field(default=30, description="Timeout in seconds")

class ScrapeResponse(BaseModel):
    url: str
    status_code: int
    content: str
    headers: Dict[str, str]
    error: Optional[str] = None

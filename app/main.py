from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.endpoints import router as api_router

app = FastAPI(
    title="PhantomScrape Lite",
    description="A lightweight web scraping API using basic TLS spoofing. This is a free, limited version.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/", include_in_schema=False)
async def root():
    # Redirect root to Swagger UI
    return RedirectResponse(url="/docs")

# Include the API routers
app.include_router(api_router, prefix="/api/v1", tags=["Scraper"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

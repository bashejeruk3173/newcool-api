from fastapi import FastAPI
from scraper import scrape_dramacool

app = FastAPI()

@app.get("/")
def homepage():
    return scrape_dramacool()

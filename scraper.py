import json
import re
import requests
from bs4 import BeautifulSoup

def get_tamil_movies():
    print("Fetching Tamil Movies for Nura TV Stream...")
    
    # TamilMV & TamilBlasters-க்கான பொதுவான தரவு தளம்
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # மாதிரி தரவு வடிவம் (Nura App UI-க்காக)
    movies_data = {
        "app_name": "Nura Tamil Movies",
        "featured": {
            "title": "Leo / The GOAT",
            "rating": "8.9",
            "year": "2024",
            "category": "Tamil (Original)",
            "poster": "https://image.tmdb.org/t/p/w500/AQL4J2JzKx1wK2wX3V4v2.jpg",
            "stream_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        },
        "tamil_movies": [],
        "tamil_dubbed": []
    }
    
    # தானாக டேட்டாவைச் சேமிக்கும் JSON கோப்பு
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(movies_data, f, ensure_ascii=False, indent=4)
        
    print("movies.json created successfully!")

if __name__ == "__main__":
    get_tamil_movies()

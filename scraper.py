import json
import re
import requests
from bs4 import BeautifulSoup

def fetch_latest_movies():
    print("Nura Scraper: Scanning for latest Tamil releases...")
    
    # TamilMV சமீபத்திய ஸ்ட்ரீம்கள் மற்றும் படங்களின் மாதிரி தரவுத்தளம்
    # இது புதிய படங்களின் போஸ்டர் மற்றும் ஸ்ட்ரீம்களைத் தொகுக்கும்
    movies_db = {
        "tamil": [
            {
                "title": "GOAT (The Greatest Of All Time)",
                "quality": "Tamil • 4K HDR",
                "poster": "https://image.tmdb.org/t/p/w500/b33nnKl1GSJbao4l3fZDDqsMx0F.jpg",
                "stream": "https://vjs.zencdn.net/v/oceans.mp4"
            },
            {
                "title": "Amaran (2024)",
                "quality": "Tamil • 1080p HD",
                "poster": "https://m.media-amazon.com/images/M/MV5BMjA5MjYwMTEtNjBkYS00NTg4LWIxZTUtNjY3MGQ4M2Q1NDVjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "stream": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4"
            },
            {
                "title": "Maharaja (2024)",
                "quality": "Tamil • 1080p HD",
                "poster": "https://m.media-amazon.com/images/M/MV5BNGQxNDgzZWQtZTNjNi00M2NmLWExMTgtOTY4NjA4ZDcxN2Q5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "stream": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4"
            }
        ],
        "dubbed": [
            {
                "title": "Deadpool & Wolverine",
                "quality": "Tamil Dub • 4K UHD",
                "poster": "https://image.tmdb.org/t/p/w500/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg",
                "stream": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4"
            },
            {
                "title": "Kalki 2898 AD",
                "quality": "Tamil Dub • 1080p",
                "poster": "https://m.media-amazon.com/images/M/MV5BNmU5OTQzYjctM2M0Ni00OTZkLWE1MjktMTJmNDYxYmU5NjY5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "stream": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
            }
        ]
    }
    
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(movies_db, f, ensure_ascii=False, indent=2)
    print("movies.json updated successfully!")

if __name__ == "__main__":
    fetch_latest_movies()

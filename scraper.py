import json
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup

def get_poster(movie_title):
    try:
        # சுத்தமான படத்தின் பெயரை மட்டும் பிரித்தல்
        clean_name = re.sub(r'\[.*?\]|\(.*?\)|WEB-DL|HDRip|PreDVD|Tamil|HQ|Rips', '', movie_title).strip()
        search_query = urllib.parse.quote(clean_name)
        # TMDB அல்லது இலவச போஸ்டர் API வழியாக ஒரிஜினல் போஸ்டர் எடுத்தல்
        api_url = f"https://itunes.apple.com/search?term={search_query}&media=movie&limit=1"
        res = requests.get(api_url, timeout=5).json()
        if res['resultCount'] > 0:
            return res['results'][0]['artworkUrl100'].replace('100x100bb', '600x900bb')
    except Exception:
        pass
    return "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=400&q=80"

def scrape_tamilmv():
    print("Fetching TamilMV live updates with Posters...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = "https://www.1tamilmv.ing"
    
    movies_db = {"tamil": [], "dubbed": []}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        
        added = set()
        for a in links:
            title = a.get_text(strip=True)
            if any(k in title for k in ['Tamil', 'Dub', 'HDRip', 'WEB-DL', 'PreDVD']) and len(title) > 10:
                if title not in added:
                    poster_img = get_poster(title)
                    item = {
                        "title": title[:30] + "...",
                        "quality": "Tamil • HQ",
                        "poster": poster_img,
                        "stream": "https://vjs.zencdn.net/v/oceans.mp4"
                    }
                    if "Dub" in title or "Telugu" in title or "Hindi" in title:
                        movies_db["dubbed"].append(item)
                    else:
                        movies_db["tamil"].append(item)
                    
                    added.add(title)
                    if len(added) >= 12:
                        break
    except Exception as e:
        print("Error:", e)

    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(movies_db, f, ensure_ascii=False, indent=2)
    print("Done: JSON updated with posters!")

if __name__ == "__main__":
    scrape_tamilmv()

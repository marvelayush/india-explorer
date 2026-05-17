import os
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import seed_data

# Wikipedia User-Agent policy requires a detailed User-Agent header:
# https://meta.wikimedia.org/wiki/User-Agent_policy
HEADERS = {
    'User-Agent': 'IndiaExplorerImageFetcher/1.0 (ayush@example.com; contact: ayush@example.com) Python-requests/2.31'
}

def get_wiki_image_and_desc(query, retry=2):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": 1,
        "prop": "pageimages|extracts",
        "exintro": 1,
        "explaintext": 1,
        "format": "json",
        "pithumbsize": 800
    }
    for _ in range(retry):
        try:
            r = requests.get(url, headers=HEADERS, params=params, timeout=3)
            if r.status_code == 200:
                data = r.json()
                pages = data.get("query", {}).get("pages", {})
                for page_id, page_info in pages.items():
                    img = page_info.get("thumbnail", {}).get("source", None)
                    desc = page_info.get("extract", None)
                    return img, desc
            elif r.status_code == 429:
                time.sleep(1)
        except Exception:
            pass
    return None, None

def get_resolved_wiki_title(query):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": 1,
        "format": "json"
    }
    try:
        r = requests.get(url, headers=HEADERS, params=params, timeout=3)
        if r.status_code == 200:
            data = r.json()
            pages = data.get("query", {}).get("pages", {})
            for page_id, page_info in pages.items():
                return page_info.get("title", None)
    except Exception:
        pass
    return None

def get_wiki_gallery_images(title, max_images=3):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "images",
        "format": "json"
    }
    try:
        r = requests.get(url, headers=HEADERS, params=params, timeout=3)
        if r.status_code == 200:
            data = r.json()
            pages = data.get("query", {}).get("pages", {})
            for page_id, page_info in pages.items():
                images = page_info.get("images", [])
                valid_images = []
                for img in images:
                    img_title = img.get("title", "")
                    if img_title.lower().endswith(('.jpg', '.jpeg', '.png')):
                        lower_title = img_title.lower()
                        if any(x in lower_title for x in ['logo', 'icon', 'stub', 'flag', 'sign', 'marker', 'map']):
                            continue
                        valid_images.append(img_title)
                
                urls = []
                if valid_images:
                    img_titles = "|".join(valid_images[:max_images * 2])
                    img_params = {
                        "action": "query",
                        "titles": img_titles,
                        "prop": "imageinfo",
                        "iiprop": "url",
                        "iiurlwidth": 800,
                        "format": "json"
                    }
                    r_img = requests.get(url, headers=HEADERS, params=img_params, timeout=3)
                    if r_img.status_code == 200:
                        img_data = r_img.json()
                        img_pages = img_data.get("query", {}).get("pages", {})
                        for img_page_id, img_page_info in img_pages.items():
                            info = img_page_info.get("imageinfo", [])
                            if info:
                                thumb = info[0].get("thumburl", info[0].get("url"))
                                if thumb:
                                    urls.append(thumb)
                                    if len(urls) >= max_images:
                                        break
                return urls
    except Exception:
        pass
    return []

def fetch_place(place):
    query = place["name"]
    queries = [query]
    
    # Standard spelling conversions (Gurudwara -> Gurdwara, etc.)
    if "gurudwara" in query.lower():
        queries.append(query.lower().replace("gurudwara", "gurdwara"))
        queries.append(query.lower().replace("gurudwara", ""))
    if "temple" in query.lower():
        queries.append(query.lower().replace("temple", "mandir"))
        queries.append(query.lower().replace("temple", ""))
    
    img, desc = None, None
    for q in queries:
        img, desc = get_wiki_image_and_desc(q)
        if img and desc:
            break
            
    if not img or not desc:
        for q in queries:
            img, desc = get_wiki_image_and_desc(f"{q}, {place['city']}")
            if img and desc:
                break
                
    if not img or not desc:
        state_title = place['state_slug'].replace('-', ' ').title()
        for q in queries:
            img, desc = get_wiki_image_and_desc(f"{q}, {state_title}")
            if img and desc:
                break
                
    # Get 2-3 additional gallery images
    gallery_images = []
    if img:
        resolved_title = None
        for q in queries:
            resolved_title = get_resolved_wiki_title(q)
            if resolved_title:
                break
        if not resolved_title:
            for q in queries:
                resolved_title = get_resolved_wiki_title(f"{q}, {place['city']}")
                if resolved_title:
                    break
        if resolved_title:
            gallery_images = get_wiki_gallery_images(resolved_title)
            
    return place["slug"], img, desc, gallery_images, place["name"]

def fetch_state(state):
    # Manually correct Jammu & Kashmir to beautiful mountain scenic image
    if state["slug"] == "jammu-and-kashmir":
        return state["slug"], "https://upload.wikimedia.org/wikipedia/commons/6/60/Pir_Panjal_2478293509_8000ae5902_o.jpg", state["name"]
    
    img, _ = get_wiki_image_and_desc(state["name"] + " state")
    if not img:
        img, _ = get_wiki_image_and_desc(state["name"] + " India")
    if not img:
        img, _ = get_wiki_image_and_desc(state["name"])
    return state["slug"], img, state["name"]

def main():
    states, places = seed_data.get_seed_data()
    
    progress_file = "new_images.json"
    state_images = {}
    place_images = {}
    place_descriptions = {}
    place_galleries = {}
    
    print(f"Starting fetch for {len(states)} states and {len(places)} places with high accuracy and gallery extraction...")

    # 1. Fetch States
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_state, state): state for state in states}
        for i, future in enumerate(as_completed(futures)):
            slug, img, name = future.result()
            if img:
                state_images[slug] = img
                print(f"[State {i+1}/{len(states)}] Success: '{name}' -> {img}")
            else:
                print(f"[State {i+1}/{len(states)}] No image found for '{name}'")
            
            with open(progress_file, "w") as f:
                json.dump({
                    "states": state_images,
                    "places": place_images,
                    "descriptions": place_descriptions,
                    "galleries": place_galleries
                }, f, indent=4)

    # 2. Fetch Places
    completed_count = 0
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(fetch_place, place): place for place in places}
        for future in as_completed(futures):
            slug, img, desc, gallery, name = future.result()
            completed_count += 1
            
            if img:
                place_images[slug] = img
            if desc:
                place_descriptions[slug] = desc
            if gallery:
                place_galleries[slug] = gallery
                
            print(f"[{completed_count}/{len(places)}] Processed: '{name}' (Has Image: {img is not None}, Has Description: {desc is not None}, Gallery Size: {len(gallery)})")
            
            if completed_count % 10 == 0 or completed_count == len(places):
                with open(progress_file, "w") as f:
                    json.dump({
                        "states": state_images,
                        "places": place_images,
                        "descriptions": place_descriptions,
                        "galleries": place_galleries
                    }, f, indent=4)

    print(f"Done! Successfully updated {progress_file}. States: {len(state_images)}, Places: {len(place_images)}, Descriptions: {len(place_descriptions)}, Galleries: {len(place_galleries)}")

if __name__ == "__main__":
    main()

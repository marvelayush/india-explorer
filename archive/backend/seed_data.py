from uuid import uuid4


def _id():
    return str(uuid4())

PLACE_IMAGES = {
    "agam-kuan-patna": "/images/agam-kuan.jpg"
}


I = {
    "taj": "https://images.pexels.com/photos/30638768/pexels-photo-30638768.jpeg?auto=compress&w=800",
    "kerala": "https://images.pexels.com/photos/35080149/pexels-photo-35080149.jpeg?auto=compress&w=800",
    "jaipur": "https://images.unsplash.com/photo-1677868821169-08885cfcb495?w=800&h=600&fit=crop",
    "rooftop": "https://images.unsplash.com/photo-1763692050909-17d36f53600c?w=800&h=600&fit=crop",
    "qutub": "https://images.unsplash.com/photo-1763234110864-b3b9844b2b0c?w=800&h=600&fit=crop",
    "taj2": "https://images.unsplash.com/photo-1732308988547-bfbcf9171f69?w=800&h=600&fit=crop",
    "redfort": "https://images.unsplash.com/photo-1770021601254-8eba1d9ba5fc?w=800&h=600&fit=crop",
    "valley": "https://images.unsplash.com/photo-1627276007188-3f66e98a97b2?w=800&h=600&fit=crop",
    "mtn": "https://images.unsplash.com/photo-1568644559664-e4a5735c37ea?w=800&h=600&fit=crop",
    "green": "https://images.unsplash.com/photo-1627270446748-3daf2932b30e?w=800&h=600&fit=crop",
    "river": "https://images.unsplash.com/photo-1563998945887-c01b498eb6a3?w=800&h=600&fit=crop",
    "sun": "https://images.unsplash.com/photo-1723871568974-886dc3351ec3?w=800&h=600&fit=crop",
    "hampi": "https://images.unsplash.com/photo-1718206798156-5c234d735dae?w=800&h=600&fit=crop",
    "hall": "https://images.unsplash.com/photo-1621495619455-2869cd1d7a93?w=800&h=600&fit=crop",
    "tower": "https://images.unsplash.com/photo-1668948824982-37c263b8dfb4?w=800&h=600&fit=crop",
    "beach1": "https://images.unsplash.com/photo-1727276883315-53b22b811f43?w=800&h=600&fit=crop",
    "beach2": "https://images.unsplash.com/photo-1663580793278-156fef3f6394?w=800&h=600&fit=crop",
    "beach3": "https://images.unsplash.com/photo-1586940740068-283fa41052de?w=800&h=600&fit=crop",
    "beach4": "https://images.unsplash.com/photo-1701440138424-d851930f25cf?w=800&h=600&fit=crop",
}

CAT_IMGS = {
    "Heritage": ["rooftop", "redfort", "hall", "jaipur", "taj2"],
    "UNESCO": ["taj", "sun", "hampi", "hall", "redfort"],
    "Nature": ["kerala", "valley", "green", "river", "mtn", "beach1"],
    "Wildlife": ["valley", "green", "mtn", "river"],
    "Recreation": ["rooftop", "valley", "jaipur", "redfort"],
    "Beach": ["beach1", "beach2", "beach3", "beach4"],
}

DESCS = {
    "Heritage": [
        "{0} stands as a proud symbol of {1}'s rich cultural heritage and architectural legacy.",
        "{0} in {1} is a celebrated historical landmark showcasing remarkable architecture.",
        "Explore the timeless grandeur of {0} in {1}, a testament to India's illustrious past.",
        "{0} near {1} offers a fascinating glimpse into centuries of history and tradition.",
    ],
    "UNESCO": [
        "{0} is a UNESCO World Heritage Site near {1}, recognized for its outstanding universal value.",
        "A crown jewel of world heritage, {0} in {1} captivates with extraordinary significance.",
    ],
    "Nature": [
        "{0} near {1} offers breathtaking natural beauty and serene landscapes for nature lovers.",
        "Immerse yourself in the pristine splendor of {0} in {1}, a paradise for outdoor enthusiasts.",
        "{0} in {1} enchants visitors with stunning vistas and tranquil natural surroundings.",
    ],
    "Wildlife": [
        "{0} near {1} is a vital wildlife sanctuary, home to diverse species in their natural habitat.",
        "A premier wildlife destination, {0} near {1} offers thrilling safaris and rare sightings.",
    ],
    "Recreation": [
        "{0} is a vibrant destination in {1}, offering engaging experiences for visitors of all ages.",
        "Discover {0} in {1}, where entertainment meets culture in a delightful setting.",
    ],
    "Beach": [
        "{0} features pristine shores and azure waters near {1}, ideal for relaxation and water sports.",
        "Sun, sand, and serenity await at {0} near {1}, one of India's finest coastal gems.",
    ],
}

SEASONS = {
    "bihar": "October to March", "rajasthan": "October to March", "uttar-pradesh": "October to March",
    "maharashtra": "November to February", "tamil-nadu": "November to February", "kerala": "September to March",
    "goa": "November to February", "himachal-pradesh": "March to June", "uttarakhand": "March to June",
    "west-bengal": "October to March", "madhya-pradesh": "October to March", "karnataka": "October to February",
    "gujarat": "October to March", "jammu-and-kashmir": "April to October", "ladakh": "June to September",
    "andhra-pradesh": "October to February", "telangana": "October to March", "odisha": "October to March",
    "punjab": "October to March", "assam": "October to April", "meghalaya": "October to May",
    "sikkim": "March to May", "jharkhand": "October to March", "chhattisgarh": "November to February",
    "andaman-and-nicobar-islands": "October to May", "lakshadweep": "October to May", "delhi": "October to March",
    "haryana": "October to March", "arunachal-pradesh": "March to October", "nagaland": "October to May",
    "manipur": "October to March", "tripura": "September to March", "puducherry": "October to March",
    "chandigarh": "October to March", "mizoram": "October to March",
    "dadra-and-nagar-haveli-and-daman-and-diu": "October to May",
}

PLACE_IMAGES = {
    "agam-kuan-patna": "https://www.google.com/imgres?q=agam%20kuan&imgurl=https%3A%2F%2Fs7ap1.scene7.com%2Fis%2Fimage%2Fincredibleindia%2Fagam-kuan-patna-bihar-2-musthead-hero%3Fqlt%3D82%26ts%3D1742162595232&imgrefurl=https%3A%2F%2Fwww.incredibleindia.gov.in%2Fen%2Fbihar%2Fpatna%2Fagam-kuan&docid=yssEyh43YnizTM&tbnid=NKCnubD2SDhq1M&vet=12ahUKEwjsm9ORqsCUAxUEVmwGHQArI6MQnPAOegQIIhAB..i&w=1280&h=720&hcb=2&ved=2ahUKEwjsm9ORqsCUAxUEVmwGHQArI6MQnPAOegQIIhAB"
}

def get_seed_data():
    import json
    import urllib.parse
    from pathlib import Path
    
    current_dir = Path(__file__).parent
    new_images_path = current_dir / "new_images.json"
    new_images = {}
    if new_images_path.exists():
        try:
            with open(new_images_path, "r", encoding="utf-8") as f:
                new_images = json.load(f)
        except Exception:
            pass

    states = [
        {"id": _id(), "name": "Bihar", "slug": "bihar", "capital": "Patna", "description": "Cradle of Buddhism and Jainism, home to ancient universities and sacred sites.", "image_url": I["sun"], "region": "East", "highlights": ["Bodh Gaya", "Nalanda", "Rajgir"]},
        {"id": _id(), "name": "Rajasthan", "slug": "rajasthan", "capital": "Jaipur", "description": "The Land of Kings - magnificent forts, colorful deserts, and royal palaces.", "image_url": I["jaipur"], "region": "West", "highlights": ["Forts & Palaces", "Desert Safari", "Royal Heritage"]},
        {"id": _id(), "name": "Uttar Pradesh", "slug": "uttar-pradesh", "capital": "Lucknow", "description": "Home to the Taj Mahal, the ghats of Varanasi, and Mughal grandeur.", "image_url": I["taj"], "region": "Central", "highlights": ["Taj Mahal", "Varanasi Ghats", "Mughal Heritage"]},
        {"id": _id(), "name": "Maharashtra", "slug": "maharashtra", "capital": "Mumbai", "description": "Land of Marathas, Bollywood, and ancient rock-cut cave temples.", "image_url": I["redfort"], "region": "West", "highlights": ["Gateway of India", "Ajanta Caves", "Bollywood"]},
        {"id": _id(), "name": "Tamil Nadu", "slug": "tamil-nadu", "capital": "Chennai", "description": "Dravidian temple architecture, classical arts, and pristine beaches.", "image_url": I["tower"], "region": "South", "highlights": ["Meenakshi Temple", "Marina Beach", "Hill Stations"]},
        {"id": _id(), "name": "Kerala", "slug": "kerala", "capital": "Thiruvananthapuram", "description": "God's Own Country - serene backwaters, lush tea gardens, and Ayurveda.", "image_url": I["kerala"], "region": "South", "highlights": ["Backwaters", "Munnar Tea", "Ayurveda"]},
        {"id": _id(), "name": "Goa", "slug": "goa", "capital": "Panaji", "description": "India's beach paradise blending Portuguese heritage with tropical vibes.", "image_url": I["beach1"], "region": "West", "highlights": ["Golden Beaches", "Portuguese Churches", "Nightlife"]},
        {"id": _id(), "name": "Himachal Pradesh", "slug": "himachal-pradesh", "capital": "Shimla", "description": "Dev Bhoomi - Land of Gods, with snow-capped peaks and hill stations.", "image_url": I["mtn"], "region": "North", "highlights": ["Shimla", "Manali", "Dharamshala"]},
        {"id": _id(), "name": "Uttarakhand", "slug": "uttarakhand", "capital": "Dehradun", "description": "Dev Bhoomi with sacred rivers, yoga capital Rishikesh, and Himalayan trails.", "image_url": I["valley"], "region": "North", "highlights": ["Rishikesh", "Jim Corbett", "Char Dham"]},
        {"id": _id(), "name": "West Bengal", "slug": "west-bengal", "capital": "Kolkata", "description": "Cultural capital with the Victoria Memorial, Darjeeling tea, and Sundarbans.", "image_url": I["redfort"], "region": "East", "highlights": ["Victoria Memorial", "Darjeeling", "Sundarbans"]},
        {"id": _id(), "name": "Madhya Pradesh", "slug": "madhya-pradesh", "capital": "Bhopal", "description": "Heart of India with UNESCO temples at Khajuraho and tiger reserves.", "image_url": I["hall"], "region": "Central", "highlights": ["Khajuraho", "Sanchi Stupa", "Tiger Safaris"]},
        {"id": _id(), "name": "Karnataka", "slug": "karnataka", "capital": "Bengaluru", "description": "From the ruins of Hampi to the hills of Coorg, a land of diverse beauty.", "image_url": I["hampi"], "region": "South", "highlights": ["Hampi Ruins", "Mysore Palace", "Coorg Coffee"]},
        {"id": _id(), "name": "Gujarat", "slug": "gujarat", "capital": "Gandhinagar", "description": "Land of legends, from the white desert of Kutch to Asiatic lions of Gir.", "image_url": I["sun"], "region": "West", "highlights": ["Rann of Kutch", "Gir Lions", "Statue of Unity"]},
        {"id": _id(), "name": "Jammu and Kashmir", "slug": "jammu-and-kashmir", "capital": "Srinagar", "description": "Paradise on Earth - pristine Dal Lake, Mughal gardens, and snowy peaks.", "image_url": I["river"], "region": "North", "highlights": ["Dal Lake", "Gulmarg", "Mughal Gardens"]},
        {"id": _id(), "name": "Ladakh", "slug": "ladakh", "capital": "Leh", "description": "Land of high passes with surreal landscapes, monasteries, and Pangong Lake.", "image_url": I["mtn"], "region": "North", "highlights": ["Pangong Lake", "Nubra Valley", "Monasteries"]},
        {"id": _id(), "name": "Andhra Pradesh", "slug": "andhra-pradesh", "capital": "Amaravati", "description": "Known for its rich heritage, Tirupati temple, and stunning Araku Valley.", "image_url": I["tower"], "region": "South", "highlights": ["Tirupati Temple", "Araku Valley", "Amaravati"]},
        {"id": _id(), "name": "Telangana", "slug": "telangana", "capital": "Hyderabad", "description": "Land of the Nizams with iconic Charminar and world-class biryani.", "image_url": I["rooftop"], "region": "South", "highlights": ["Charminar", "Golconda Fort", "Hyderabadi Cuisine"]},
        {"id": _id(), "name": "Odisha", "slug": "odisha", "capital": "Bhubaneswar", "description": "Temple state of India with the magnificent Sun Temple and Chilika Lake.", "image_url": I["sun"], "region": "East", "highlights": ["Konark Sun Temple", "Jagannath Temple", "Chilika Lake"]},
        {"id": _id(), "name": "Punjab", "slug": "punjab", "capital": "Chandigarh", "description": "Land of five rivers, the Golden Temple, and warm Punjabi hospitality.", "image_url": I["rooftop"], "region": "North", "highlights": ["Golden Temple", "Wagah Border", "Punjabi Cuisine"]},
        {"id": _id(), "name": "Assam", "slug": "assam", "capital": "Dispur", "description": "Gateway to Northeast India, famous for tea gardens and one-horned rhinos.", "image_url": I["valley"], "region": "Northeast", "highlights": ["Kaziranga Rhinos", "Tea Gardens", "Majuli Island"]},
        {"id": _id(), "name": "Meghalaya", "slug": "meghalaya", "capital": "Shillong", "description": "Abode of Clouds with living root bridges and the wettest place on Earth.", "image_url": I["green"], "region": "Northeast", "highlights": ["Living Root Bridges", "Cherrapunji", "Dawki River"]},
        {"id": _id(), "name": "Sikkim", "slug": "sikkim", "capital": "Gangtok", "description": "Himalayan jewel with monasteries, orchids, and views of Kanchenjunga.", "image_url": I["river"], "region": "Northeast", "highlights": ["Tsomgo Lake", "Nathula Pass", "Monasteries"]},
        {"id": _id(), "name": "Jharkhand", "slug": "jharkhand", "capital": "Ranchi", "description": "Land of forests and waterfalls, with rich mineral wealth and tribal culture.", "image_url": I["green"], "region": "East", "highlights": ["Hundru Falls", "Deoghar", "Betla NP"]},
        {"id": _id(), "name": "Chhattisgarh", "slug": "chhattisgarh", "capital": "Raipur", "description": "Undiscovered gem with waterfalls, caves, and rich tribal heritage.", "image_url": I["valley"], "region": "Central", "highlights": ["Chitrakote Falls", "Tribal Art", "Dense Forests"]},
        {"id": _id(), "name": "Andaman and Nicobar Islands", "slug": "andaman-and-nicobar-islands", "capital": "Port Blair", "description": "Tropical paradise with crystal clear waters, coral reefs, and WWII history.", "image_url": I["beach2"], "region": "Island", "highlights": ["Radhanagar Beach", "Cellular Jail", "Scuba Diving"]},
        {"id": _id(), "name": "Lakshadweep", "slug": "lakshadweep", "capital": "Kavaratti", "description": "Pristine coral atolls with turquoise lagoons and untouched marine life.", "image_url": I["beach3"], "region": "Island", "highlights": ["Agatti Island", "Coral Reefs", "Water Sports"]},
        {"id": _id(), "name": "Delhi", "slug": "delhi", "capital": "New Delhi", "description": "India's capital - ancient Mughal monuments blended with modern cosmopolitan life.", "image_url": I["qutub"], "region": "North", "highlights": ["Red Fort", "Qutub Minar", "India Gate"]},
        {"id": _id(), "name": "Haryana", "slug": "haryana", "capital": "Chandigarh", "description": "Historic battleground of Kurukshetra and gateway to northern India.", "image_url": I["valley"], "region": "North", "highlights": ["Kurukshetra", "Sultanpur Birds", "Kingdom of Dreams"]},
        {"id": _id(), "name": "Arunachal Pradesh", "slug": "arunachal-pradesh", "capital": "Itanagar", "description": "Land of the Dawn-Lit Mountains with pristine monasteries and tribal culture.", "image_url": I["green"], "region": "Northeast", "highlights": ["Tawang Monastery", "Ziro Valley", "Tribal Culture"]},
        {"id": _id(), "name": "Nagaland", "slug": "nagaland", "capital": "Kohima", "description": "Land of Festivals, famous for the Hornbill Festival and warrior tribes.", "image_url": I["valley"], "region": "Northeast", "highlights": ["Hornbill Festival", "Dzukou Valley", "Naga Heritage"]},
        {"id": _id(), "name": "Manipur", "slug": "manipur", "capital": "Imphal", "description": "Jewel of India with the floating lake Loktak and ancient Kangla Fort.", "image_url": I["valley"], "region": "Northeast", "highlights": ["Loktak Lake", "Kangla Fort", "Sangai Festival"]},
        {"id": _id(), "name": "Tripura", "slug": "tripura", "capital": "Agartala", "description": "Home to the lake palace Neermahal and lush green hills of Northeast.", "image_url": I["valley"], "region": "Northeast", "highlights": ["Neermahal Palace", "Ujjayanta Palace", "Tribal Culture"]},
        {"id": _id(), "name": "Mizoram", "slug": "mizoram", "capital": "Aizawl", "description": "Land of the hill people, known for stunning landscapes and vibrant culture.", "image_url": I["mtn"], "region": "Northeast", "highlights": ["Phawngpui Peak", "Tam Dil Lake", "Bamboo Forests"]},
        {"id": _id(), "name": "Puducherry", "slug": "puducherry", "capital": "Puducherry", "description": "French Riviera of the East with colonial charm and spiritual Auroville.", "image_url": I["beach4"], "region": "South", "highlights": ["French Quarter", "Auroville", "Promenade Beach"]},
        {"id": _id(), "name": "Chandigarh", "slug": "chandigarh", "capital": "Chandigarh", "description": "Le Corbusier's planned city, famous for Rock Garden and Sukhna Lake.", "image_url": I["valley"], "region": "North", "highlights": ["Rock Garden", "Sukhna Lake", "Le Corbusier"]},
        {"id": _id(), "name": "Dadra and Nagar Haveli and Daman and Diu", "slug": "dadra-and-nagar-haveli-and-daman-and-diu", "capital": "Daman", "description": "Coastal union territory with Portuguese forts, beaches, and tribal villages.", "image_url": I["beach4"], "region": "West", "highlights": ["Diu Fort", "Nagoa Beach", "Portuguese Heritage"]},
    ]

    for state in states:
        slug = state["slug"]
        if "states" in new_images and slug in new_images["states"]:
            state["image_url"] = new_images["states"][slug]

    R = """bihar|Patna|Patna Sahib Gurudwara|Heritage
bihar|Patna|Buddha Smriti Park|Recreation
bihar|Patna|Golghar|Heritage
bihar|Patna|Patna Museum|Recreation
bihar|Patna|Agam Kuan|Heritage
bihar|Patna|Padri Ki Haveli Church|Heritage
bihar|Patna|Sanjay Gandhi Biological Park|Wildlife
bihar|Rajgir|Shanti Stupa|UNESCO
bihar|Rajgir|Rajgir Zoo Safari|Wildlife
bihar|Rajgir|Glass Bridge|Recreation
bihar|Rajgir|Gridhakuta Hill|Heritage
bihar|Rajgir|Venuvan Vihar|Heritage
bihar|Rajgir|Nalanda Ruins|UNESCO
bihar|Rajgir|Hot Springs|Nature
bihar|Rajgir|Vishwa Shanti Stupa|Heritage
bihar|Bodh Gaya|Mahabodhi Temple|UNESCO
bihar|Bodh Gaya|Bodhi Tree|UNESCO
bihar|Bodh Gaya|Great Buddha Statue|Heritage
bihar|Bodh Gaya|Thai Monastery|Heritage
bihar|Bodh Gaya|Japanese Temple|Heritage
bihar|Bodh Gaya|Niranjana River|Nature
bihar|Vaishali|Ashoka Pillar|Heritage
bihar|Vaishali|Buddha Relic Stupa|Heritage
bihar|Vaishali|Vaishali Museum|Recreation
bihar|Vaishali|Raja Vishal Ka Garh|Heritage
bihar|Pawapuri|Jal Mandir|Heritage
bihar|Pawapuri|Apapapuri Temple|Heritage
rajasthan|Jaipur|Amber Fort|UNESCO
rajasthan|Jaipur|Hawa Mahal|Heritage
rajasthan|Jaipur|City Palace Jaipur|Heritage
rajasthan|Jaipur|Jantar Mantar|UNESCO
rajasthan|Jaipur|Nahargarh Fort|Heritage
rajasthan|Jaipur|Jaigarh Fort|Heritage
rajasthan|Jaipur|Albert Hall Museum|Recreation
rajasthan|Jaipur|Birla Mandir Jaipur|Heritage
rajasthan|Udaipur|City Palace Udaipur|Heritage
rajasthan|Udaipur|Lake Pichola|Nature
rajasthan|Udaipur|Sajjangarh Fort|Heritage
rajasthan|Udaipur|Fateh Sagar Lake|Nature
rajasthan|Udaipur|Jagdish Temple|Heritage
rajasthan|Udaipur|Vintage Car Museum|Recreation
rajasthan|Jodhpur|Mehrangarh Fort|Heritage
rajasthan|Jodhpur|Jaswant Thada|Heritage
rajasthan|Jodhpur|Umaid Bhawan Palace|Heritage
rajasthan|Jodhpur|Mandore Gardens|Nature
rajasthan|Jodhpur|Clock Tower Jodhpur|Recreation
rajasthan|Jaisalmer|Jaisalmer Fort|UNESCO
rajasthan|Jaisalmer|Sam Sand Dunes|Nature
rajasthan|Jaisalmer|Patwon Ki Haveli|Heritage
rajasthan|Jaisalmer|Gadisar Lake|Nature
rajasthan|Jaisalmer|Desert National Park|Wildlife
rajasthan|Ranthambore|Ranthambore National Park|Wildlife
rajasthan|Ranthambore|Ranthambore Fort|Heritage
rajasthan|Ranthambore|Padam Talao|Nature
rajasthan|Pushkar|Brahma Temple|Heritage
rajasthan|Pushkar|Pushkar Lake|Nature
rajasthan|Pushkar|Savitri Temple|Heritage
uttar-pradesh|Agra|Taj Mahal|UNESCO
uttar-pradesh|Agra|Agra Fort|UNESCO
uttar-pradesh|Agra|Fatehpur Sikri|UNESCO
uttar-pradesh|Agra|Itmad-ud-Daula|Heritage
uttar-pradesh|Agra|Mehtab Bagh|Nature
uttar-pradesh|Agra|Akbar Tomb Sikandra|Heritage
uttar-pradesh|Varanasi|Kashi Vishwanath Temple|Heritage
uttar-pradesh|Varanasi|Dashashwamedh Ghat|Heritage
uttar-pradesh|Varanasi|Sarnath|UNESCO
uttar-pradesh|Varanasi|Manikarnika Ghat|Heritage
uttar-pradesh|Varanasi|Ramnagar Fort|Heritage
uttar-pradesh|Varanasi|Assi Ghat|Heritage
uttar-pradesh|Lucknow|Bara Imambara|Heritage
uttar-pradesh|Lucknow|Chhota Imambara|Heritage
uttar-pradesh|Lucknow|Rumi Darwaza|Heritage
uttar-pradesh|Lucknow|Residency Ruins|Heritage
uttar-pradesh|Lucknow|Hazratganj Market|Recreation
uttar-pradesh|Lucknow|Lucknow Zoo|Wildlife
uttar-pradesh|Mathura-Vrindavan|Krishna Janmabhoomi|Heritage
uttar-pradesh|Mathura-Vrindavan|Banke Bihari Temple|Heritage
uttar-pradesh|Mathura-Vrindavan|ISKCON Temple Vrindavan|Heritage
uttar-pradesh|Mathura-Vrindavan|Govardhan Hill|Heritage
uttar-pradesh|Ayodhya|Ram Mandir|Heritage
uttar-pradesh|Ayodhya|Hanumangadhi Temple|Heritage
uttar-pradesh|Ayodhya|Kanak Bhawan|Heritage
uttar-pradesh|Ayodhya|Saryu River Ghats|Heritage
uttar-pradesh|Prayagraj|Triveni Sangam|Heritage
uttar-pradesh|Prayagraj|Allahabad Fort|Heritage
uttar-pradesh|Prayagraj|Anand Bhawan|Recreation
uttar-pradesh|Prayagraj|Khusro Bagh|Heritage
maharashtra|Mumbai|Gateway of India|Heritage
maharashtra|Mumbai|Elephanta Caves|UNESCO
maharashtra|Mumbai|Marine Drive|Recreation
maharashtra|Mumbai|Chhatrapati Shivaji Terminus|UNESCO
maharashtra|Mumbai|Colaba Causeway|Recreation
maharashtra|Mumbai|Sanjay Gandhi National Park|Wildlife
maharashtra|Mumbai|Juhu Beach|Nature
maharashtra|Aurangabad|Ajanta Caves|UNESCO
maharashtra|Aurangabad|Ellora Caves|UNESCO
maharashtra|Aurangabad|Bibi Ka Maqbara|Heritage
maharashtra|Aurangabad|Daulatabad Fort|Heritage
maharashtra|Aurangabad|Grishneshwar Temple|Heritage
maharashtra|Pune|Shaniwar Wada|Heritage
maharashtra|Pune|Aga Khan Palace|Heritage
maharashtra|Pune|Osho Ashram|Recreation
maharashtra|Pune|Pataleshwar Caves|Heritage
maharashtra|Pune|Sinhagad Fort|Heritage
maharashtra|Nashik|Trimbakeshwar Temple|Heritage
maharashtra|Nashik|Pandavleni Caves|Heritage
maharashtra|Nashik|Ramkund|Heritage
maharashtra|Nashik|Dugarwadi Waterfall|Nature
maharashtra|Lonavala|Bhushi Dam|Nature
maharashtra|Lonavala|Karla Caves|Heritage
maharashtra|Lonavala|Bhaja Caves|Heritage
maharashtra|Lonavala|Rajmachi Fort|Heritage
maharashtra|Lonavala|Tigers Leap|Nature
tamil-nadu|Chennai|Marina Beach|Nature
tamil-nadu|Chennai|Kapaleeshwarar Temple|Heritage
tamil-nadu|Chennai|Fort St George|Heritage
tamil-nadu|Chennai|Arignar Anna Zoological Park|Wildlife
tamil-nadu|Chennai|Government Museum Chennai|Recreation
tamil-nadu|Madurai|Meenakshi Amman Temple|Heritage
tamil-nadu|Madurai|Thirumalai Nayakkar Mahal|Heritage
tamil-nadu|Madurai|Gandhi Memorial Museum|Recreation
tamil-nadu|Madurai|Alagar Kovil|Heritage
tamil-nadu|Mahabalipuram|Shore Temple|UNESCO
tamil-nadu|Mahabalipuram|Five Rathas|UNESCO
tamil-nadu|Mahabalipuram|Arjunas Penance|UNESCO
tamil-nadu|Mahabalipuram|Tiger Cave|Heritage
tamil-nadu|Ooty|Nilgiri Mountain Railway|UNESCO
tamil-nadu|Ooty|Ooty Lake|Nature
tamil-nadu|Ooty|Botanical Garden Ooty|Nature
tamil-nadu|Ooty|Doddabetta Peak|Nature
tamil-nadu|Ooty|Mudumalai Wildlife Sanctuary|Wildlife
tamil-nadu|Rameswaram|Ramanathaswamy Temple|Heritage
tamil-nadu|Rameswaram|Pamban Bridge|Recreation
tamil-nadu|Rameswaram|Dhanushkodi|Nature
tamil-nadu|Rameswaram|Agnitheertham Beach|Nature
tamil-nadu|Kanchipuram|Kailasanathar Temple|Heritage
tamil-nadu|Kanchipuram|Ekambareswarar Temple|Heritage
tamil-nadu|Kanchipuram|Kamakshi Amman Temple|Heritage
kerala|Munnar|Tea Gardens Munnar|Nature
kerala|Munnar|Eravikulam National Park|Wildlife
kerala|Munnar|Mattupetty Dam|Nature
kerala|Munnar|Anamudi Peak|Nature
kerala|Munnar|Tea Museum Munnar|Recreation
kerala|Alleppey|Backwaters Houseboat|Nature
kerala|Alleppey|Alappuzha Beach|Nature
kerala|Alleppey|Krishnapuram Palace|Heritage
kerala|Alleppey|Vembanad Lake|Nature
kerala|Thekkady|Periyar Wildlife Sanctuary|Wildlife
kerala|Thekkady|Periyar Lake|Nature
kerala|Thekkady|Spice Plantation Tour|Recreation
kerala|Thrissur|Thrissur Pooram Festival Ground|Heritage
kerala|Thrissur|Vadakkunnathan Temple|Heritage
kerala|Thrissur|Athirapally Waterfalls|Nature
kerala|Thrissur|Sakthan Thampuran Palace|Heritage
kerala|Kovalam|Kovalam Beach|Beach
kerala|Kovalam|Vizhinjam Rock Cut Cave|Heritage
kerala|Kovalam|Halcyon Castle|Heritage
kerala|Wayanad|Edakkal Caves|Heritage
kerala|Wayanad|Chembra Peak|Nature
kerala|Wayanad|Banasura Sagar Dam|Nature
kerala|Wayanad|Wayanad Wildlife Sanctuary|Wildlife
goa|North Goa|Baga Beach|Beach
goa|North Goa|Calangute Beach|Beach
goa|North Goa|Fort Aguada|Heritage
goa|North Goa|Chapora Fort|Heritage
goa|North Goa|Anjuna Flea Market|Recreation
goa|North Goa|Basilica of Bom Jesus|UNESCO
goa|North Goa|Se Cathedral|UNESCO
goa|South Goa|Palolem Beach|Beach
goa|South Goa|Colva Beach|Beach
goa|South Goa|Dudhsagar Waterfalls|Nature
goa|South Goa|Butterfly Beach|Beach
goa|South Goa|Cabo de Rama Fort|Heritage
goa|Old Goa|Churches of Old Goa|UNESCO
goa|Old Goa|Convent of St Francis of Assisi|UNESCO
goa|Old Goa|Goa State Museum|Recreation
himachal-pradesh|Shimla|The Ridge Shimla|Recreation
himachal-pradesh|Shimla|Mall Road Shimla|Recreation
himachal-pradesh|Shimla|Jakhoo Temple|Heritage
himachal-pradesh|Shimla|Kufri|Nature
himachal-pradesh|Shimla|Christ Church Shimla|Heritage
himachal-pradesh|Shimla|Kalka Shimla Railway|UNESCO
himachal-pradesh|Manali|Rohtang Pass|Nature
himachal-pradesh|Manali|Solang Valley|Nature
himachal-pradesh|Manali|Hadimba Temple|Heritage
himachal-pradesh|Manali|Beas River|Nature
himachal-pradesh|Manali|Old Manali|Recreation
himachal-pradesh|Manali|Great Himalayan National Park|Wildlife
himachal-pradesh|Dharamshala|Tsuglagkhang Complex|Heritage
himachal-pradesh|Dharamshala|Dal Lake Dharamshala|Nature
himachal-pradesh|Dharamshala|Bhagsu Waterfall|Nature
himachal-pradesh|Dharamshala|War Memorial Dharamshala|Recreation
himachal-pradesh|Dharamshala|St John Church|Heritage
himachal-pradesh|Spiti Valley|Key Monastery|Heritage
himachal-pradesh|Spiti Valley|Chandratal Lake|Nature
himachal-pradesh|Spiti Valley|Pin Valley National Park|Wildlife
himachal-pradesh|Spiti Valley|Dhankar Monastery|Heritage
himachal-pradesh|Spiti Valley|Hikkim Post Office|Recreation
himachal-pradesh|Kasauli|Christ Church Kasauli|Heritage
himachal-pradesh|Kasauli|Monkey Point|Nature
himachal-pradesh|Kasauli|Gilbert Trail|Nature
himachal-pradesh|Bir Billing|Paragliding Capital of India|Recreation
himachal-pradesh|Bir Billing|Chokling Monastery|Heritage
himachal-pradesh|Bir Billing|Tibetan Colony|Heritage
uttarakhand|Rishikesh|Laxman Jhula|Heritage
uttarakhand|Rishikesh|Ram Jhula|Heritage
uttarakhand|Rishikesh|Triveni Ghat|Heritage
uttarakhand|Rishikesh|Rafting on Ganga|Recreation
uttarakhand|Rishikesh|Beatles Ashram|Recreation
uttarakhand|Rishikesh|Neelkanth Mahadev Temple|Heritage
uttarakhand|Haridwar|Har Ki Pauri|Heritage
uttarakhand|Haridwar|Ganga Aarti Haridwar|Heritage
uttarakhand|Haridwar|Mansa Devi Temple|Heritage
uttarakhand|Haridwar|Chandi Devi Temple|Heritage
uttarakhand|Haridwar|Rajaji National Park|Wildlife
uttarakhand|Jim Corbett|Dhikala Zone|Wildlife
uttarakhand|Jim Corbett|Bijrani Zone|Wildlife
uttarakhand|Jim Corbett|Jhirna Zone|Wildlife
uttarakhand|Jim Corbett|Sitabani Buffer Zone|Wildlife
uttarakhand|Nainital|Naini Lake|Nature
uttarakhand|Nainital|Snow View Point|Nature
uttarakhand|Nainital|Naina Devi Temple|Heritage
uttarakhand|Nainital|Bhimtal Lake|Nature
uttarakhand|Mussoorie|Kempty Falls|Nature
uttarakhand|Mussoorie|Gun Hill|Nature
uttarakhand|Mussoorie|Mall Road Mussoorie|Recreation
uttarakhand|Mussoorie|Lal Tibba|Nature
uttarakhand|Mussoorie|Camels Back Road|Recreation
uttarakhand|Char Dham|Badrinath|Heritage
uttarakhand|Char Dham|Kedarnath|Heritage
uttarakhand|Char Dham|Gangotri|Heritage
uttarakhand|Char Dham|Yamunotri|Heritage
uttarakhand|Char Dham|Valley of Flowers|Wildlife
west-bengal|Kolkata|Victoria Memorial|Heritage
west-bengal|Kolkata|Howrah Bridge|Recreation
west-bengal|Kolkata|Dakshineswar Temple|Heritage
west-bengal|Kolkata|Indian Museum|Recreation
west-bengal|Kolkata|Eden Gardens|Recreation
west-bengal|Kolkata|Marble Palace|Heritage
west-bengal|Kolkata|Science City Kolkata|Recreation
west-bengal|Darjeeling|Darjeeling Himalayan Railway|UNESCO
west-bengal|Darjeeling|Tiger Hill|Nature
west-bengal|Darjeeling|Tea Gardens Darjeeling|Nature
west-bengal|Darjeeling|Batasia Loop|Recreation
west-bengal|Darjeeling|Peace Pagoda|Heritage
west-bengal|Darjeeling|Padmaja Naidu Zoo|Wildlife
west-bengal|Sundarbans|Sundarbans National Park|Wildlife
west-bengal|Sundarbans|Sudhanyakhali Watch Tower|Wildlife
west-bengal|Sundarbans|Sajnekhali Bird Sanctuary|Wildlife
west-bengal|Shantiniketan|Visva Bharati University|Recreation
west-bengal|Shantiniketan|Rabindranath Tagore Home|Heritage
west-bengal|Shantiniketan|Sriniketan|Recreation
madhya-pradesh|Khajuraho|Khajuraho Temple Group|UNESCO
madhya-pradesh|Khajuraho|Panna National Park|Wildlife
madhya-pradesh|Khajuraho|Raneh Falls|Nature
madhya-pradesh|Khajuraho|Archaeological Museum Khajuraho|Recreation
madhya-pradesh|Bhopal|Upper Lake Bhojtal|Nature
madhya-pradesh|Bhopal|Van Vihar National Park|Wildlife
madhya-pradesh|Bhopal|Bhimbetka Caves|UNESCO
madhya-pradesh|Bhopal|Sanchi Stupa|UNESCO
madhya-pradesh|Bhopal|Taj ul Masajid|Heritage
madhya-pradesh|Gwalior|Gwalior Fort|Heritage
madhya-pradesh|Gwalior|Jai Vilas Palace|Heritage
madhya-pradesh|Gwalior|Teli Ka Mandir|Heritage
madhya-pradesh|Gwalior|Gopachal Hill|Heritage
madhya-pradesh|Kanha|Kanha Tiger Reserve|Wildlife
madhya-pradesh|Kanha|Bamni Dadar|Wildlife
madhya-pradesh|Kanha|Shravan Tal|Nature
madhya-pradesh|Bandhavgarh|Bandhavgarh Tiger Reserve|Wildlife
madhya-pradesh|Bandhavgarh|Bandhavgarh Fort|Heritage
madhya-pradesh|Bandhavgarh|Shesh Shaiya Statue|Heritage
madhya-pradesh|Orchha|Orchha Fort|Heritage
madhya-pradesh|Orchha|Chaturbhuj Temple|Heritage
madhya-pradesh|Orchha|Raja Ram Temple|Heritage
madhya-pradesh|Orchha|Orchha Wildlife Sanctuary|Wildlife
karnataka|Bengaluru|Lalbagh Botanical Garden|Nature
karnataka|Bengaluru|Cubbon Park|Nature
karnataka|Bengaluru|Tipu Sultan Palace|Heritage
karnataka|Bengaluru|ISKCON Temple Bengaluru|Heritage
karnataka|Bengaluru|Vidhana Soudha|Recreation
karnataka|Bengaluru|Bannerghatta National Park|Wildlife
karnataka|Mysuru|Mysore Palace|Heritage
karnataka|Mysuru|Chamundeshwari Temple|Heritage
karnataka|Mysuru|Brindavan Gardens|Nature
karnataka|Mysuru|Nagarhole National Park|Wildlife
karnataka|Mysuru|St Philomena Church|Heritage
karnataka|Hampi|Hampi Group of Monuments|UNESCO
karnataka|Hampi|Virupaksha Temple|Heritage
karnataka|Hampi|Vittala Temple Stone Chariot|UNESCO
karnataka|Hampi|Lotus Mahal|Heritage
karnataka|Hampi|Elephant Stables|Heritage
karnataka|Coorg|Abbey Falls|Nature
karnataka|Coorg|Rajas Seat|Nature
karnataka|Coorg|Namdroling Monastery|Heritage
karnataka|Coorg|Talacauvery|Heritage
karnataka|Coorg|Dubare Elephant Camp|Wildlife
karnataka|Badami|Badami Cave Temples|Heritage
karnataka|Badami|Aihole|Heritage
karnataka|Badami|Pattadakal|UNESCO
karnataka|Badami|Agastya Lake|Nature
gujarat|Ahmedabad|Sabarmati Ashram|Heritage
gujarat|Ahmedabad|Adalaj Stepwell|Heritage
gujarat|Ahmedabad|Akshardham Temple Ahmedabad|Heritage
gujarat|Ahmedabad|Kite Museum|Recreation
gujarat|Ahmedabad|Calico Museum of Textiles|Recreation
gujarat|Rann of Kutch|White Rann|Nature
gujarat|Rann of Kutch|Dholavira|UNESCO
gujarat|Rann of Kutch|Kalo Dungar|Nature
gujarat|Rann of Kutch|Wild Ass Sanctuary|Wildlife
gujarat|Gir|Gir National Park|Wildlife
gujarat|Gir|Somnath Temple|Heritage
gujarat|Gir|Diu Island|Nature
gujarat|Vadodara|Laxmi Vilas Palace|Heritage
gujarat|Vadodara|Baroda Museum|Recreation
gujarat|Vadodara|Sayaji Baug|Nature
gujarat|Dwarka|Dwarkadhish Temple|Heritage
gujarat|Dwarka|Gomti Ghat|Heritage
gujarat|Dwarka|Nageshwar Jyotirlinga|Heritage
gujarat|Dwarka|Beyt Dwarka Island|Nature
jammu-and-kashmir|Srinagar|Dal Lake Houseboats|Nature
jammu-and-kashmir|Srinagar|Mughal Gardens|Nature
jammu-and-kashmir|Srinagar|Shankaracharya Temple|Heritage
jammu-and-kashmir|Srinagar|Hazratbal Shrine|Heritage
jammu-and-kashmir|Srinagar|Nagin Lake|Nature
jammu-and-kashmir|Srinagar|Chashme Shahi|Nature
jammu-and-kashmir|Gulmarg|Gulmarg Gondola|Recreation
jammu-and-kashmir|Gulmarg|Apharwat Peak|Nature
jammu-and-kashmir|Gulmarg|Strawberry Valley|Nature
jammu-and-kashmir|Pahalgam|Betaab Valley|Nature
jammu-and-kashmir|Pahalgam|Aru Valley|Nature
jammu-and-kashmir|Pahalgam|Baisaran|Nature
jammu-and-kashmir|Pahalgam|Lidder River|Nature
ladakh|Leh|Pangong Tso Lake|Nature
ladakh|Leh|Thiksey Monastery|Heritage
ladakh|Leh|Hemis Monastery|Heritage
ladakh|Leh|Nubra Valley|Nature
ladakh|Leh|Magnetic Hill|Recreation
ladakh|Leh|Hemis National Park|Wildlife
ladakh|Leh|Khardung La Pass|Nature
andhra-pradesh|Tirupati|Tirumala Venkateswara Temple|Heritage
andhra-pradesh|Tirupati|Talakona Waterfall|Nature
andhra-pradesh|Tirupati|Srikalahasti Temple|Heritage
andhra-pradesh|Amaravati|Amaravati Stupa|Heritage
andhra-pradesh|Amaravati|Amaravati Museum|Recreation
telangana|Hyderabad|Charminar|Heritage
telangana|Hyderabad|Golconda Fort|Heritage
telangana|Hyderabad|Qutb Shahi Tombs|Heritage
telangana|Hyderabad|Hussain Sagar Lake|Nature
telangana|Hyderabad|Birla Mandir Hyderabad|Heritage
telangana|Hyderabad|Nehru Zoological Park|Wildlife
telangana|Warangal|Warangal Fort|Heritage
telangana|Warangal|Ramappa Temple|UNESCO
telangana|Warangal|Thousand Pillar Temple|Heritage
telangana|Warangal|Pakhal Lake|Nature
odisha|Puri|Jagannath Temple|Heritage
odisha|Puri|Puri Beach|Nature
odisha|Puri|Chilika Lake|Wildlife
odisha|Puri|Raghurajpur Heritage Village|Heritage
odisha|Bhubaneswar|Lingaraj Temple|Heritage
odisha|Bhubaneswar|Udayagiri Khandagiri Caves|Heritage
odisha|Bhubaneswar|Odisha State Museum|Recreation
odisha|Bhubaneswar|Nandankanan Zoo|Wildlife
odisha|Konark|Konark Sun Temple|UNESCO
odisha|Konark|Archaeological Museum Konark|Recreation
odisha|Konark|Konark Beach|Nature
punjab|Amritsar|Golden Temple|Heritage
punjab|Amritsar|Jallianwala Bagh|Heritage
punjab|Amritsar|Wagah Border Ceremony|Recreation
punjab|Amritsar|Durgiana Temple|Heritage
punjab|Amritsar|Gobindgarh Fort|Heritage
punjab|Anandpur Sahib|Takht Sri Kesgarh Sahib|Heritage
punjab|Anandpur Sahib|Virasat-e-Khalsa Museum|Recreation
assam|Kaziranga|Kaziranga National Park|Wildlife
assam|Kaziranga|Elephant Safari Kaziranga|Wildlife
assam|Kaziranga|Jeep Safari Kaziranga|Wildlife
assam|Guwahati|Kamakhya Temple|Heritage
assam|Guwahati|Umananda Island Temple|Heritage
assam|Guwahati|Assam State Museum|Recreation
assam|Guwahati|Nehru Park Guwahati|Recreation
assam|Majuli Island|Satras Monasteries|Heritage
assam|Majuli Island|Dakhinpat Satra|Heritage
assam|Majuli Island|Cultural Festivals Majuli|Recreation
meghalaya|Shillong|Cherrapunji|Nature
meghalaya|Shillong|Living Root Bridges|Nature
meghalaya|Shillong|Elephant Falls|Nature
meghalaya|Shillong|Umiam Lake|Nature
meghalaya|Shillong|Nohkalikai Falls|Nature
sikkim|Gangtok|Rumtek Monastery|Heritage
sikkim|Gangtok|Tsomgo Lake|Nature
sikkim|Gangtok|Nathula Pass|Nature
sikkim|Gangtok|Kanchenjunga National Park|Wildlife
sikkim|Gangtok|Pelling Pemayangtse|Heritage
jharkhand|Ranchi|Hundru Falls|Nature
jharkhand|Ranchi|Jonha Falls|Nature
jharkhand|Ranchi|Rock Garden Ranchi|Recreation
jharkhand|Ranchi|Jagannath Temple Ranchi|Heritage
jharkhand|Deoghar|Baidyanath Jyotirlinga Temple|Heritage
jharkhand|Deoghar|Nandan Pahar|Nature
jharkhand|Deoghar|Satsang Ashram|Heritage
chhattisgarh|Jagdalpur|Chitrakot Falls|Nature
chhattisgarh|Jagdalpur|Tirathgarh Falls|Nature
chhattisgarh|Jagdalpur|Kanger Valley National Park|Wildlife
chhattisgarh|Jagdalpur|Dantewada Temple|Heritage
chhattisgarh|Raipur|Ghatarani Waterfall|Nature
chhattisgarh|Raipur|Rajim Temples|Heritage
chhattisgarh|Raipur|Barnawapara Wildlife Sanctuary|Wildlife
andaman-and-nicobar-islands|Port Blair|Cellular Jail|Heritage
andaman-and-nicobar-islands|Port Blair|Ross Island|Heritage
andaman-and-nicobar-islands|Port Blair|Corbyns Cove Beach|Nature
andaman-and-nicobar-islands|Port Blair|Anthropological Museum|Recreation
andaman-and-nicobar-islands|Havelock Island|Radhanagar Beach|Beach
andaman-and-nicobar-islands|Havelock Island|Elephant Beach|Beach
andaman-and-nicobar-islands|Havelock Island|Scuba Diving Snorkeling|Recreation
andaman-and-nicobar-islands|Neil Island|Natural Bridge|Nature
andaman-and-nicobar-islands|Neil Island|Bharatpur Beach|Beach
lakshadweep|Agatti Island|Agatti Beach|Beach
lakshadweep|Agatti Island|Lagoon Snorkeling|Recreation
lakshadweep|Bangaram Island|Bangaram Beach|Beach
lakshadweep|Bangaram Island|Coral Reef Diving|Recreation
delhi|New Delhi|Red Fort Delhi|UNESCO
delhi|New Delhi|Qutub Minar|UNESCO
delhi|New Delhi|Humayuns Tomb|UNESCO
delhi|New Delhi|India Gate|Recreation
delhi|New Delhi|Lotus Temple|Heritage
delhi|New Delhi|Akshardham Temple Delhi|Heritage
delhi|New Delhi|Chandni Chowk|Recreation
delhi|New Delhi|National Museum Delhi|Recreation
delhi|New Delhi|Lodhi Garden|Nature
delhi|New Delhi|Mehrauli Archaeological Park|Heritage
haryana|Kurukshetra|Brahma Sarovar|Heritage
haryana|Kurukshetra|Krishna Museum|Recreation
haryana|Kurukshetra|Jyotisar|Heritage
haryana|Panipat|Panipat Museum|Recreation
haryana|Panipat|Kala Amb|Heritage
haryana|Panipat|Devi Temple Panipat|Heritage
arunachal-pradesh|Tawang|Tawang Monastery|Heritage
arunachal-pradesh|Tawang|Sela Pass|Nature
arunachal-pradesh|Tawang|Nuranang Falls|Nature
arunachal-pradesh|Tawang|Namdapha National Park|Wildlife
nagaland|Kohima|Hornbill Festival Ground|Recreation
nagaland|Kohima|War Cemetery Kohima|Heritage
nagaland|Kohima|Dzukou Valley|Nature
manipur|Imphal|Loktak Lake|Nature
manipur|Imphal|Keibul Lamjao National Park|Wildlife
manipur|Imphal|Kangla Fort|Heritage
manipur|Imphal|Ima Market|Recreation
tripura|Agartala|Ujjayanta Palace|Heritage
tripura|Agartala|Neermahal Water Palace|Heritage
tripura|Agartala|Tripura Sundari Temple|Heritage
tripura|Agartala|Sepahijala Wildlife Sanctuary|Wildlife
puducherry|Pondicherry|Auroville|Recreation
puducherry|Pondicherry|Sri Aurobindo Ashram|Heritage
puducherry|Pondicherry|Promenade Beach|Nature
puducherry|Pondicherry|French Quarter Puducherry|Heritage
puducherry|Pondicherry|Paradise Beach|Nature
chandigarh|Chandigarh|Rock Garden Chandigarh|Heritage
chandigarh|Chandigarh|Sukhna Lake|Nature
mizoram|Aizawl|Phawngpui Peak|Nature
mizoram|Aizawl|Tam Dil Lake|Nature
dadra-and-nagar-haveli-and-daman-and-diu|Diu|Diu Fort|Heritage
dadra-and-nagar-haveli-and-daman-and-diu|Diu|Nagoa Beach|Beach""".strip().split("\n")

    places = []
    for i, line in enumerate(R):
        parts = line.split("|")
        state, city, name, cat = parts[0], parts[1], parts[2], parts[3]
        slug = (name + " " + city).lower()
        for ch in "(),&'/.":
            slug = slug.replace(ch, "")
        slug = "-".join(slug.split())

        keys = CAT_IMGS.get(cat, ["valley"])
        if "places" in new_images and slug in new_images["places"]:
            img = new_images["places"][slug]
        else:
            img = PLACE_IMAGES.get(slug, I[keys[i % len(keys)]])

        if "descriptions" in new_images and slug in new_images["descriptions"] and new_images["descriptions"][slug]:
            desc = new_images["descriptions"][slug]
        else:
            templates = DESCS.get(cat, ["{0} is a must-visit attraction in {1}."])
            desc = templates[i % len(templates)].format(name, city)

        times = "Sunrise to Sunset" if cat in ("Nature", "Beach") else "6:00 AM - 6:00 PM daily" if cat != "Wildlife" else "Check seasonal timings"

        state_names = {s["slug"]: s["name"] for s in states}
        state_name = state_names.get(state, state.replace("-", " ").title())
        gmaps_query = f"{name}, {city}, {state_name}, India"
        google_map_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(gmaps_query)}"
        wiki_url = f"https://en.wikipedia.org/wiki/Special:Search?search={urllib.parse.quote_plus(name + ' ' + city)}"

        gallery = new_images.get("galleries", {}).get(slug, [])
        places.append({
            "id": _id(), "state_slug": state, "city": city, "name": name, "slug": slug,
            "category": cat, "description": desc, "image_url": img,
            "how_to_reach": f"Accessible from {city} by local transport.",
            "opening_times": times, "contact": "Local tourism office",
            "best_time_to_visit": SEASONS.get(state, "October to March"),
            "entry_fee": "Check locally", "highlights": [],
            "google_map_url": google_map_url,
            "wiki_url": wiki_url,
            "gallery_images": gallery,
        })

    return states, places
import json
import asyncio
import server

def main():
    with open("new_images.json", "r") as f:
        data = json.load(f)

    # Manual precision overrides for famous places and Andaman islands
    overrides = {
        # Patna & Amritsar Overrides
        "patna-sahib-gurudwara-patna": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/TheJoyof350thAnniversary%40IncredibleIndia.jpg/960px-TheJoyof350thAnniversary%40IncredibleIndia.jpg",
        "golden-temple-amritsar": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/The_Golden_Temple_of_Amrithsar_7.jpg/960px-The_Golden_Temple_of_Amrithsar_7.jpg",
        "durgiana-temple-amritsar": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Many_of_the_locals_we_had_spoken_to_were_delighted_that_the_Govt_has_sanctioned_funds_for_renovation_of_this_temple_%2838049489065%29.jpg/960px-Many_of_the_locals_we_had_spoken_to_were_delighted_that_the_Govt_has_sanctioned_funds_for_renovation_of_this_temple_%2838049489065%29.jpg",
        
        # Andaman & Nicobar Islands Overrides
        "cellular-jail-port-blair": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Front_View_of_Cellular_Jail%2C_Port_Blair.JPG/960px-Front_View_of_Cellular_Jail%2C_Port_Blair.JPG",
        "ross-island-port-blair": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Ross_Island_%28Netaji_Subhas_Bose_Island%29.jpg/960px-Ross_Island_%28Netaji_Subhas_Bose_Island%29.jpg",
        "radhanagar-beach-havelock-island": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Radha_Nagar_beach%2C_Havelock_Island%2C_Andamn%2C_India-_Sun_set_view.jpg/960px-Radha_Nagar_beach%2C_Havelock_Island%2C_Andamn%2C_India-_Sun_set_view.jpg",
        "elephant-beach-havelock-island": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Havelock%2C_Andaman_%26_Nicobar_Islands.JPG/960px-Havelock%2C_Andaman_%26_Nicobar_Islands.JPG",
        "corbyns-cove-beach-port-blair": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Corbyns_cove_beach%2CPort_Blaire%2CAndaman_-_panoramio.jpg",
        "scuba-diving-snorkeling-havelock-island": "https://upload.wikimedia.org/wikipedia/commons/0/01/Scuba_diving_in_havelock_island.jpg",
        "natural-bridge-neil-island": "https://upload.wikimedia.org/wikipedia/commons/0/04/Natural_Bridge%2C_Neil_Island%2C_Andaman%2C_India.JPG",
        "bharatpur-beach-neil-island": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Neil_Island_-_Bharatpur_beach_as_seen_from_jetty.jpg",
        "anthropological-museum-port-blair": "https://upload.wikimedia.org/wikipedia/commons/9/94/Musee_National_Anthropologie-Entree.jpg",
        
        # Ellora Caves Overrides
        "ellora-caves-aurangabad": "https://upload.wikimedia.org/wikipedia/commons/3/32/Ellora%2C_Aurangabad%2C_Maharashtra.jpg"
    }

    # State overrides
    state_overrides = {
        "himachal-pradesh": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Kee_monastery_Spiti_Valley_%28edited%29.jpg",
        "arunachal-pradesh": "https://upload.wikimedia.org/wikipedia/commons/b/be/13%2C700_feet_Sela_Lake%2Cin_west_Kameng%2C_Arunachal_Pradesh.jpg"
    }

    # Add galleries for these manual overrides
    gallery_overrides = {
        "patna-sahib-gurudwara-patna": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Harmandir_Patna.jpg/960px-Harmandir_Patna.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/GuruGobindBirthPlace.jpg/960px-GuruGobindBirthPlace.jpg"
        ],
        "golden-temple-amritsar": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Golden_Temple%2C_Amritsar%2C_India.jpg/960px-Golden_Temple%2C_Amritsar%2C_India.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Golden_temple_india.jpg/960px-Golden_temple_india.jpg"
        ],
        "cellular-jail-port-blair": [
            "https://upload.wikimedia.org/wikipedia/commons/1/15/Cellular_jail%27s_hanging_cell.JPG",
            "https://upload.wikimedia.org/wikipedia/commons/9/9b/Closer_view_of_a_cell_of_Cellular_Jail%2C_Port_Blair%2C_India.jpg"
        ],
        "ross-island-port-blair": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/South_End_of_Ross_Island.jpg/960px-South_End_of_Ross_Island.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Peacocks_at_Ross_island_Port_blair.jpg/960px-Peacocks_at_Ross_island_Port_blair.jpg"
        ],
        "radhanagar-beach-havelock-island": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Havelock_Island_resort.jpg/960px-Havelock_Island_resort.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Sunset_at_Havelock.JPG/960px-Sunset_at_Havelock.JPG"
        ],
        "natural-bridge-neil-island": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Neil_Island_Bridge%2C_Andaman_Islands.jpg/960px-Neil_Island_Bridge%2C_Andaman_Islands.jpg"
        ],
        "ellora-caves-aurangabad": [
            "https://upload.wikimedia.org/wikipedia/commons/1/15/Ellora_cave16_001.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/4/40/Indra_Sabha_Ellora_Temple_Maharashtra_India.jpg"
        ]
    }

    # Override description for Andaman places if they were generic Sumatran tsunami descriptions
    description_overrides = {
        "cellular-jail-port-blair": "The Cellular Jail, also known as Kala Pani, was a colonial prison in the Andaman and Nicobar Islands, India. The prison was used by the British government for the purpose of exiling political prisoners to the remote archipelago. Many notable independence activists, including Batukeshwar Dutt, Yogendra Shukla and Vinayak Damodar Savarkar, were imprisoned here during the struggle for India's independence.",
        "ross-island-port-blair": "Netaji Subhash Chandra Bose Island, formerly known as Ross Island, is an island of the Andaman Islands. It belongs to the South Andaman administrative district, Port Blair, and is located 3 km east from central Port Blair. The historic ruins of the British administrative headquarters, church, and hospital are popular attractions.",
        "radhanagar-beach-havelock-island": "Radhanagar Beach, also known as Beach No. 7, is one of the most famous beaches in Asia. Located on Havelock Island (Swaraj Dweep) in the Andaman and Nicobar Islands, it is renowned for its pristine white sands, turquoise waters, and breathtaking sunset views.",
        "elephant-beach-havelock-island": "Elephant Beach is a popular destination on Havelock Island, famous for its vibrant coral reefs, shallow waters, and water sports. It is an ideal spot for snorkeling, sea walking, and glass-bottom boat rides.",
        "corbyns-cove-beach-port-blair": "Corbyn's Cove is a scenic, coconut-palm fringed beach located close to Port Blair city. It is popular for jet skiing, boating, and beachside relaxation, offering beautiful views of the turquoise waters.",
        "scuba-diving-snorkeling-havelock-island": "Havelock Island is the premier scuba diving destination in India. Renowned for its crystal clear waters, rich marine biodiversity, and spectacular coral reefs, it offers incredible diving experiences for beginners and professionals alike."
    }

    for k, v in overrides.items():
        data["places"][k] = v
        print(f"Overrode '{k}' main image.")

    for k, v in state_overrides.items():
        data["states"][k] = v
        print(f"Overrode state '{k}' main image.")

    for k, v in gallery_overrides.items():
        data["galleries"][k] = v
        print(f"Overrode '{k}' gallery images.")

    for k, v in description_overrides.items():
        data["descriptions"][k] = v
        print(f"Overrode '{k}' description.")

    with open("new_images.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Successfully updated new_images.json with manual overrides.")

    # Reseed
    print("Reseeding database...")
    asyncio.run(server.seed_database())
    print("Reseed complete.")

if __name__ == "__main__":
    main()

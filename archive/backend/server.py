from fastapi import FastAPI, APIRouter, Query, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

app = FastAPI()
api_router = APIRouter(prefix="/api")


@api_router.get("/")
async def root():
    return {"message": "India Explorer API"}


@api_router.get("/states")
async def get_states():
    states = await db.states.find({}, {"_id": 0}).to_list(100)
    return states


@api_router.get("/states/{slug}")
async def get_state(slug: str):
    state = await db.states.find_one({"slug": slug}, {"_id": 0})
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
    places = await db.places.find({"state_slug": slug}, {"_id": 0}).to_list(100)
    return {"state": state, "places": places}


@api_router.get("/places/{slug}")
async def get_place(slug: str):
    place = await db.places.find_one({"slug": slug}, {"_id": 0})
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    related = await db.places.find(
        {"state_slug": place["state_slug"], "slug": {"$ne": slug}}, {"_id": 0}
    ).to_list(4)
    return {"place": place, "related_places": related}


@api_router.get("/search")
async def search(q: str = Query(..., min_length=1)):
    regex = {"$regex": q, "$options": "i"}
    states = await db.states.find(
        {"$or": [{"name": regex}, {"capital": regex}, {"description": regex}]}, {"_id": 0}
    ).to_list(10)
    places = await db.places.find(
        {"$or": [{"name": regex}, {"category": regex}, {"description": regex}, {"city": regex}]}, {"_id": 0}
    ).to_list(50)
    return {"states": states, "places": places}


@api_router.get("/categories")
async def get_categories():
    categories = await db.places.distinct("category")
    return categories


@api_router.post("/seed")
async def seed_database():
    from seed_data import get_seed_data
    states_data, places_data = get_seed_data()
    await db.states.delete_many({})
    await db.places.delete_many({})
    if states_data:
        await db.states.insert_many(states_data)
    if places_data:
        await db.places.insert_many(places_data)
    return {"message": f"Seeded {len(states_data)} states and {len(places_data)} places"}


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_event():
    count = await db.states.count_documents({})
    if count == 0:
        logger.info("Database empty, auto-seeding...")
        from seed_data import get_seed_data
        states_data, places_data = get_seed_data()
        if states_data:
            await db.states.insert_many(states_data)
        if places_data:
            await db.places.insert_many(places_data)
        logger.info(f"Seeded {len(states_data)} states and {len(places_data)} places")
        await db.states.create_index([("slug", 1)], unique=True)
        await db.places.create_index([("slug", 1)], unique=True)
        await db.places.create_index([("state_slug", 1)])


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

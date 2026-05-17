# India Explorer - PRD

## Original Problem Statement
Interactive website showing all Indian states (28 states + 8 Union Territories) with tourist places, UNESCO sites, and attractions. Features include: clickable India SVG map, state detail pages with places, place detail pages with about/how to reach/opening times/contact info. Very interactive and animated.

## Architecture
- **Backend**: FastAPI + MongoDB (motor async driver)
- **Frontend**: React + Tailwind CSS + Framer Motion + Shadcn UI
- **Database**: MongoDB with `states` and `places` collections

## User Personas
- Tourists planning India trips
- Travel enthusiasts exploring destinations
- Students researching Indian geography/heritage

## Core Requirements
- [x] Interactive SVG India map with all 36 states/UTs
- [x] State detail page with tourist places
- [x] Place detail page with visitor information
- [x] Search across states and places
- [x] Category filter pills (UNESCO, Fort, Temple, Nature, etc.)
- [x] Pre-populated real data for all states
- [x] Smooth animations (Framer Motion)
- [x] Responsive design

## What's Been Implemented (April 16, 2026)
- Full backend API: /api/states, /api/states/{slug}, /api/places/{slug}, /api/search, /api/categories
- Auto-seeding: 36 states + 64 tourist places with real data
- Homepage: Hero section, interactive SVG India map, states grid, featured UNESCO sites
- **Accurate political map** using @svg-maps/india package with real state boundaries
- State detail page: Hero banner, description, highlights, category filters, places grid
- Place detail page: Hero image, about section, highlights, visitor info sidebar, related places
- Search overlay with real-time results (with working close button)
- Navigation: Navbar with back button, search trigger
- Design: Warm Sand (#FAF7F2) bg, Terracotta (#C65D47) primary, Forest Green (#2A5A43) secondary
- Typography: Cormorant Garamond (headings) + Outfit (body)
- All data-testid attributes for testing
- Testing: 100% backend, 100% frontend pass rate

## Prioritized Backlog
### P0 (Critical)
- None remaining

### P1 (Important)
- Add more images per place (image gallery carousel)
- Improve SVG map accuracy (use GeoJSON-based paths)
- Add more places per state (currently 2-3 per state)
- Mobile-optimized map interaction

### P2 (Nice to Have)
- User reviews/ratings for places
- Trip planner/itinerary builder
- Nearby hotels/restaurants integration
- Weather information per destination
- Photo upload by visitors
- Social sharing
- Dark mode toggle
- Multi-language support (Hindi, regional languages)

## Next Tasks
1. Add image galleries per place
2. Improve map with more accurate state boundaries
3. Add more tourist places (target: 5+ per major state)
4. Add "Top Picks" or "Trending" section
5. Mobile responsiveness optimization

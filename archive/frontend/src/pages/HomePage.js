import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { Search, X, MapPin, ArrowRight, Compass } from 'lucide-react';
import axios from 'axios';
import { Navbar } from '@/components/Navbar';
import { IndiaMap } from '@/components/IndiaMap';
import { PlaceCard } from '@/components/PlaceCard';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

export default function HomePage() {
  const [states, setStates] = useState([]);
  const [featuredPlaces, setFeaturedPlaces] = useState([]);
  const [searchOpen, setSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState({ states: [], places: [] });
  const [loading, setLoading] = useState(true);
  const searchRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [statesRes, featuredRes] = await Promise.all([
          axios.get(`${API}/states`),
          axios.get(`${API}/categories`),
        ]);
        setStates(statesRes.data);
        // Get some sample places for featured section
        const searchRes = await axios.get(`${API}/search?q=UNESCO`);
        setFeaturedPlaces(searchRes.data.places.slice(0, 6));
      } catch (err) {
        console.error('Failed to fetch data:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    if (!searchQuery.trim()) {
      setSearchResults({ states: [], places: [] });
      return;
    }
    const timer = setTimeout(async () => {
      try {
        const res = await axios.get(`${API}/search?q=${encodeURIComponent(searchQuery)}`);
        setSearchResults(res.data);
      } catch (err) {
        console.error('Search error:', err);
      }
    }, 300);
    return () => clearTimeout(timer);
  }, [searchQuery]);

  useEffect(() => {
    if (searchOpen && searchRef.current) searchRef.current.focus();
  }, [searchOpen]);

  return (
    <div className="min-h-screen bg-[#FAF7F2]">
      <Navbar onSearchClick={() => setSearchOpen(true)} />

      {/* Search Overlay */}
      <AnimatePresence>
        {searchOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-[100] bg-black/30 backdrop-blur-sm"
            onClick={() => setSearchOpen(false)}
          >
            <motion.div
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="max-w-2xl mx-auto mt-24 px-6"
              onClick={(e) => e.stopPropagation()}
            >
              <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
                <div className="flex items-center gap-3 px-6 py-4 border-b border-[#E6E2D8]">
                  <Search size={20} className="text-[#5C564D] flex-shrink-0" />
                  <input
                    ref={searchRef}
                    data-testid="search-input"
                    type="text"
                    placeholder="Search states, places, categories..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="flex-1 text-lg outline-none text-[#1A1814] placeholder:text-[#5C564D]/50 bg-transparent"
                  />
                  <button
                    data-testid="search-close-button"
                    onClick={(e) => { e.stopPropagation(); setSearchOpen(false); setSearchQuery(''); }}
                    className="flex-shrink-0 p-2 hover:bg-[#FAF7F2] rounded-full transition-colors cursor-pointer z-10"
                  >
                    <X size={20} className="text-[#5C564D]" />
                  </button>
                </div>
                {(searchResults.states.length > 0 || searchResults.places.length > 0) && (
                  <div className="max-h-96 overflow-y-auto p-4 space-y-3">
                    {searchResults.states.map((state) => (
                      <div
                        key={state.slug}
                        data-testid={`search-result-state-${state.slug}`}
                        onClick={() => { navigate(`/state/${state.slug}`); setSearchOpen(false); }}
                        className="flex items-center gap-3 p-3 rounded-xl hover:bg-[#FAF7F2] cursor-pointer transition-colors"
                      >
                        <MapPin size={16} className="text-[#C65D47]" />
                        <div>
                          <p className="font-medium text-[#1A1814]">{state.name}</p>
                          <p className="text-xs text-[#5C564D]">{state.capital} &middot; {state.region}</p>
                        </div>
                      </div>
                    ))}
                    {searchResults.places.map((place) => (
                      <div
                        key={place.slug}
                        data-testid={`search-result-place-${place.slug}`}
                        onClick={() => { navigate(`/place/${place.slug}`); setSearchOpen(false); }}
                        className="flex items-center gap-3 p-3 rounded-xl hover:bg-[#FAF7F2] cursor-pointer transition-colors"
                      >
                        <Compass size={16} className="text-[#2A5A43]" />
                        <div>
                          <p className="font-medium text-[#1A1814]">{place.name}</p>
                          <p className="text-xs text-[#5C564D]">{place.category}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
                {searchQuery && searchResults.states.length === 0 && searchResults.places.length === 0 && (
                  <p className="p-6 text-center text-[#5C564D]">No results found</p>
                )}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Hero Section */}
      <section className="pt-28 pb-8 px-6 md:px-12 lg:px-24">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
          className="text-center max-w-3xl mx-auto mb-12"
        >
          <span className="text-xs tracking-[0.2em] uppercase font-bold text-[#C65D47]">
            Discover Incredible India
          </span>
          <h1 className="heading-font text-5xl sm:text-6xl lg:text-7xl font-medium text-[#1A1814] mt-3 mb-5 tracking-tight">
            Explore Every State,<br />Every Wonder
          </h1>
          <p className="text-base md:text-lg text-[#5C564D] leading-relaxed max-w-xl mx-auto">
            From the snow-capped Himalayas to the tropical beaches of the south.
            Click on any state to discover its treasures.
          </p>
        </motion.div>
      </section>

      {/* Map Section */}
      <section className="px-6 md:px-12 lg:px-24 pb-16">
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          <IndiaMap />
        </motion.div>
      </section>

      {/* States Grid */}
      <section className="px-6 md:px-12 lg:px-24 py-16">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="text-xs tracking-[0.2em] uppercase font-bold text-[#C65D47]">
            All States & Territories
          </span>
          <h2 className="heading-font text-3xl sm:text-4xl font-medium text-[#1A1814] mt-2 mb-8 tracking-tight">
            Browse by Region
          </h2>
        </motion.div>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
          {states.map((state, i) => (
            <motion.div
              key={state.slug}
              data-testid={`state-card-${state.slug}`}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              whileHover={{
                y: -6,
                scale: 1.025,
                boxShadow: "0 15px 30px rgba(0, 0, 0, 0.04)",
                borderColor: "rgba(198, 93, 71, 0.2)"
              }}
              whileTap={{ scale: 0.97 }}
              transition={{
                type: "spring",
                stiffness: 400,
                damping: 22
              }}
              onClick={() => navigate(`/state/${state.slug}`)}
              className="group cursor-pointer p-4 rounded-2xl border border-[#E6E2D8] bg-white transition-all duration-200"
            >
              <div className="img-zoom rounded-xl mb-3 h-24">
                <img
                  src={state.image_url}
                  alt={state.name}
                  className="w-full h-full object-cover rounded-xl"
                  loading="lazy"
                  onError={(e) => {
                    e.target.src = 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=400&h=300&fit=crop';
                  }}
                />
              </div>
              <h3 className="heading-font text-base font-medium text-[#1A1814] group-hover:text-[#C65D47] transition-colors truncate">
                {state.name}
              </h3>
              <p className="text-xs text-[#5C564D] mt-0.5">{state.capital}</p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Featured Places */}
      {featuredPlaces.length > 0 && (
        <section className="px-6 md:px-12 lg:px-24 py-16 bg-white/50">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <span className="text-xs tracking-[0.2em] uppercase font-bold text-[#C65D47]">
              Must Visit
            </span>
            <h2 className="heading-font text-3xl sm:text-4xl font-medium text-[#1A1814] mt-2 mb-8 tracking-tight">
              UNESCO Heritage Sites
            </h2>
          </motion.div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredPlaces.map((place, i) => (
              <PlaceCard key={place.slug} place={place} index={i} />
            ))}
          </div>
        </section>
      )}

      {/* Footer */}
      <footer className="px-6 md:px-12 lg:px-24 py-12 border-t border-[#E6E2D8]">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <MapPin size={18} className="text-[#C65D47]" />
            <span className="heading-font text-lg font-semibold text-[#1A1814]">India Explorer</span>
          </div>
          <p className="text-sm text-[#5C564D]">
            Discover the beauty of India &middot; All 28 States & 8 Union Territories
          </p>
        </div>
      </footer>
    </div>
  );
}

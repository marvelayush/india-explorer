import { useState, useEffect, useMemo } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { MapPin, Filter } from 'lucide-react';
import axios from 'axios';
import { Navbar } from '@/components/Navbar';
import { PlaceCard } from '@/components/PlaceCard';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

const ALL_CATEGORIES = ['All', 'UNESCO', 'Fort', 'Temple', 'Nature', 'Beach', 'Heritage', 'Hill Station', 'Wildlife'];

export default function StatePage() {
  const { slug } = useParams();
  const navigate = useNavigate();
  const [state, setState] = useState(null);
  const [places, setPlaces] = useState([]);
  const [activeFilter, setActiveFilter] = useState('All');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchState = async () => {
      setLoading(true);
      try {
        const res = await axios.get(`${API}/states/${slug}`);
        setState(res.data.state);
        setPlaces(Array.isArray(res.data.places) ? res.data.places : []);
      } catch (err) {
        console.error('Failed to fetch state:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchState();
  }, [slug]);
  const safePlaces = Array.isArray(places) ? places : [];

const filteredPlaces = activeFilter === 'All'
    ? safePlaces
    : safePlaces.filter(p => p.category === activeFilter);

  const availableCategories = ['All', ...new Set(safePlaces.map(p => p.category))];

  const groupedByCity = useMemo(() => {
    const groups = {};
    filteredPlaces.forEach(place => {
      const city = place.city || 'Other';
      if (!groups[city]) groups[city] = [];
      groups[city].push(place);
    });
    return groups;
  }, [filteredPlaces]);

  const cityCount = Object.keys(groupedByCity).length;

  if (loading) {
    return (
      <div className="min-h-screen bg-[#FAF7F2] flex items-center justify-center">
        <div className="w-8 h-8 border-2 border-[#C65D47] border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (!state) {
    return (
      <div className="min-h-screen bg-[#FAF7F2] flex flex-col items-center justify-center gap-4">
        <p className="text-[#5C564D]">State not found</p>
        <button onClick={() => navigate('/home')} className="px-6 py-2 bg-[#C65D47] text-white rounded-full text-sm">
          Back to Map
        </button>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#FAF7F2]">
      <Navbar showBack />

      {/* Hero */}
      <section className="relative pt-20">
        <div className="relative h-64 md:h-80 overflow-hidden">
          <img
            src={state.image_url}
            alt={state.name}
            className="w-full h-full object-cover"
            onError={(e) => {
              e.target.src = 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=1200&h=600&fit=crop';
            }}
          />
          <div className="absolute inset-0 bg-gradient-to-t from-[#1A1814]/80 via-[#1A1814]/30 to-transparent" />
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="absolute bottom-0 left-0 right-0 px-6 md:px-12 lg:px-24 pb-8"
          >
            <span className="text-xs tracking-[0.2em] uppercase font-bold text-[#E89A3C]">
              {state.region} India
            </span>
            <h1 className="heading-font text-4xl sm:text-5xl lg:text-6xl font-medium text-white mt-1 tracking-tight">
              {state.name}
            </h1>
            <div className="flex items-center gap-2 mt-2">
              <MapPin size={14} className="text-white/70" />
              <span className="text-sm text-white/80">Capital: {state.capital}</span>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Description & Highlights */}
      <section className="px-6 md:px-12 lg:px-24 py-8">
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="text-base md:text-lg text-[#5C564D] leading-relaxed max-w-3xl"
        >
          {state.description}
        </motion.p>
        {state.highlights && state.highlights.length > 0 && (
          <div className="flex flex-wrap gap-2 mt-4">
            {(Array.isArray(state.highlights) ? state.highlights : []).map((h, i) => (
              <span key={i} className="px-3 py-1 rounded-full text-xs font-medium bg-[#2A5A43]/10 text-[#2A5A43]">
                {h}
              </span>
            ))}
          </div>
        )}
      </section>

      {/* Filters */}
      <section className="px-6 md:px-12 lg:px-24 pb-4">
        <div className="flex items-center gap-2 mb-4">
          <Filter size={16} className="text-[#5C564D]" />
          <span className="text-sm font-medium text-[#5C564D]">Filter by category</span>
        </div>
        <div className="flex gap-2 overflow-x-auto hide-scrollbar pb-2">
          {availableCategories.map((cat) => (
            <motion.button
              key={cat}
              whileHover={{ scale: 1.04, y: -1 }}
              whileTap={{ scale: 0.96 }}
              transition={{ type: "spring", stiffness: 450, damping: 20 }}
              data-testid={`filter-button-${cat.toLowerCase().replace(/\s+/g, '-')}`}
              onClick={() => setActiveFilter(cat)}
              className={`category-pill whitespace-nowrap px-5 py-2 rounded-full text-sm font-medium border transition-all ${
                activeFilter === cat
                  ? 'bg-[#C65D47] text-white border-[#C65D47] shadow-sm'
                  : 'bg-white text-[#5C564D] border-[#E6E2D8] hover:border-[#C65D47]/30'
              }`}
            >
              {cat}
            </motion.button>
          ))}
        </div>
      </section>

      {/* Places Grid */}
      <section className="px-6 md:px-12 lg:px-24 py-8">
        <div className="flex items-center justify-between mb-6">
          <h2 className="heading-font text-2xl sm:text-3xl font-medium text-[#1A1814] tracking-tight">
            Places to Visit
          </h2>
          <span className="text-sm text-[#5C564D]">{cityCount} cities &middot; {filteredPlaces.length} places</span>
        </div>
        {Object.keys(groupedByCity).length > 0 ? (
          <div className="space-y-10">
            {Object.entries(groupedByCity).map(([city, cityPlaces]) => (
              <div key={city}>
                <div className="flex items-center gap-2 mb-4 pb-2 border-b border-[#E6E2D8]">
                  <MapPin size={16} className="text-[#C65D47]" />
                  <h3 className="heading-font text-xl font-medium text-[#1A1814]">{city}</h3>
                  <span className="text-xs text-[#5C564D] bg-[#FAF7F2] px-2 py-0.5 rounded-full">{cityPlaces.length} places</span>
                </div>
                <motion.div layout className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
                  <AnimatePresence mode="popLayout">
                    {(Array.isArray(cityPlaces) ? cityPlaces : []).map((place, i) => (
                      <PlaceCard key={place.slug} place={place} index={i} />
                    ))}
                  </AnimatePresence>
                </motion.div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-16">
            <p className="text-[#5C564D]">No places found in this category</p>
            <button
              onClick={() => setActiveFilter('All')}
              className="mt-4 px-6 py-2 rounded-full text-sm font-medium bg-[#C65D47] text-white hover:bg-[#a84a37] transition-colors"
            >
              Show All Places
            </button>
          </div>
        )}
      </section>

      {/* Back to Map */}
      <section className="px-6 md:px-12 lg:px-24 py-12 text-center">
        <button
          data-testid="explore-more-states-btn"
          onClick={() => navigate('/')}
          className="px-8 py-3 rounded-full text-sm font-medium bg-[#C65D47] text-white hover:bg-[#a84a37] transition-colors"
        >
          Explore More States
        </button>
      </section>
    </div>
  );
}

import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { MapPin, Clock, Phone, Calendar, Ticket, Navigation, ArrowRight } from 'lucide-react';
import axios from 'axios';
import { Navbar } from '@/components/Navbar';
import { PlaceCard } from '@/components/PlaceCard';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

const InfoRow = ({ icon: Icon, label, value }) => (
  <div className="flex gap-3 py-3 border-b border-[#E6E2D8] last:border-0">
    <div className="flex-shrink-0 w-8 h-8 rounded-full bg-[#C65D47]/10 flex items-center justify-center">
      <Icon size={14} className="text-[#C65D47]" />
    </div>
    <div>
      <p className="text-xs uppercase tracking-wider text-[#5C564D] font-medium">{label}</p>
      <p className="text-sm text-[#1A1814] mt-0.5 leading-relaxed">{value}</p>
    </div>
  </div>
);

export default function PlacePage() {
  const { slug } = useParams();
  const navigate = useNavigate();
  const [place, setPlace] = useState(null);
  const [relatedPlaces, setRelatedPlaces] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPlace = async () => {
      setLoading(true);
      try {
        const res = await axios.get(`${API}/places/${slug}`);
        setPlace(res.data.place);
        setRelatedPlaces(res.data.related_places || []);
      } catch (err) {
        console.error('Failed to fetch place:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchPlace();
    window.scrollTo(0, 0);
  }, [slug]);

  if (loading) {
    return (
      <div className="min-h-screen bg-[#FAF7F2] flex items-center justify-center">
        <div className="w-8 h-8 border-2 border-[#C65D47] border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (!place) {
    return (
      <div className="min-h-screen bg-[#FAF7F2] flex flex-col items-center justify-center gap-4">
        <p className="text-[#5C564D]">Place not found</p>
        <button onClick={() => navigate('/')} className="px-6 py-2 bg-[#C65D47] text-white rounded-full text-sm">
          Back to Map
        </button>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#FAF7F2]">
      <Navbar showBack />

      {/* Hero Image */}
      <section className="relative pt-20">
        <div className="relative h-72 md:h-96 overflow-hidden">
          <motion.img
            initial={{ scale: 1.1 }}
            animate={{ scale: 1 }}
            transition={{ duration: 1 }}
            src={place.image_url}
            alt={place.name}
            className="w-full h-full object-cover"
            onError={(e) => {
              e.target.src = 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=1200&h=600&fit=crop';
            }}
          />
          <div className="absolute inset-0 bg-gradient-to-t from-[#1A1814]/80 via-[#1A1814]/20 to-transparent" />
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="absolute bottom-0 left-0 right-0 px-6 md:px-12 lg:px-24 pb-8"
          >
            <span className="inline-block px-3 py-1 rounded-full text-xs font-bold tracking-wider uppercase bg-[#C65D47] text-white mb-3">
              {place.category}
            </span>
            <h1 data-testid="place-detail-title" className="heading-font text-4xl sm:text-5xl lg:text-6xl font-medium text-white tracking-tight">
              {place.name}
            </h1>
          </motion.div>
        </div>
      </section>

      {/* Content */}
      <section className="px-6 md:px-12 lg:px-24 py-12">
        <div className="flex flex-col lg:flex-row gap-12 max-w-6xl">
          {/* Main Content (Left) */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.3 }}
            className="flex-1 lg:w-2/3"
          >
            <h2 className="heading-font text-2xl sm:text-3xl font-medium text-[#1A1814] mb-4">About</h2>
            <p className="text-base md:text-lg text-[#5C564D] leading-relaxed">{place.description}</p>

            {/* Highlights */}
            {place.highlights && place.highlights.length > 0 && (
              <div className="mt-8">
                <h3 className="heading-font text-xl font-medium text-[#1A1814] mb-4">Highlights</h3>
                <div className="flex flex-wrap gap-3">
                  {place.highlights.map((h, i) => (
                    <motion.div
                      key={i}
                      initial={{ opacity: 0, scale: 0.9 }}
                      animate={{ opacity: 1, scale: 1 }}
                      transition={{ delay: 0.4 + i * 0.1 }}
                      className="flex items-center gap-2 px-4 py-2 rounded-2xl bg-[#2A5A43]/10 text-[#2A5A43]"
                    >
                      <ArrowRight size={12} />
                      <span className="text-sm font-medium">{h}</span>
                    </motion.div>
                  ))}
                </div>
              </div>
            )}

            {/* Interactive Location Map */}
            <div className="mt-8">
              <h3 className="heading-font text-xl font-medium text-[#1A1814] mb-4">Interactive Location Map</h3>
              <div className="w-full h-80 rounded-2xl overflow-hidden border border-[#E6E2D8] shadow-sm bg-[#FAF7F2]">
                <iframe
                  title="Interactive Location Map"
                  src={`https://maps.google.com/maps?q=${encodeURIComponent(place.name + ', ' + place.city + ', India')}&t=&z=15&ie=UTF8&iwloc=&output=embed`}
                  width="100%"
                  height="100%"
                  style={{ border: 0 }}
                  allowFullScreen=""
                  loading="lazy"
                />
              </div>
            </div>

            {/* Additional Photos Gallery */}
            {place.gallery_images && place.gallery_images.length > 0 && (
              <div className="mt-8">
                <h3 className="heading-font text-xl font-medium text-[#1A1814] mb-4">Gallery</h3>
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                  {place.gallery_images.map((imgUrl, i) => (
                    <motion.div
                      key={i}
                      whileHover={{ scale: 1.03 }}
                      transition={{ duration: 0.2 }}
                      className="h-48 rounded-2xl overflow-hidden border border-[#E6E2D8] shadow-sm bg-white cursor-pointer"
                      onClick={() => window.open(imgUrl, '_blank')}
                    >
                      <img
                        src={imgUrl}
                        alt={`${place.name} gallery ${i + 1}`}
                        className="w-full h-full object-cover"
                        loading="lazy"
                        onError={(e) => {
                          e.target.style.display = 'none';
                        }}
                      />
                    </motion.div>
                  ))}
                </div>
              </div>
            )}

            {/* Back to state */}
            <div className="mt-8">
              <button
                data-testid="back-to-state-btn"
                onClick={() => navigate(`/state/${place.state_slug}`)}
                className="px-6 py-2.5 rounded-full text-sm font-medium bg-[#C65D47] text-white hover:bg-[#a84a37] transition-colors"
              >
                Explore more in this state
              </button>
            </div>
          </motion.div>

          {/* Sidebar (Right) */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            className="lg:w-1/3"
          >
            <div className="lg:sticky lg:top-24 bg-white rounded-2xl border border-[#E6E2D8] p-6">
              <h3 className="heading-font text-lg font-medium text-[#1A1814] mb-4">Visitor Information</h3>
              <InfoRow icon={Navigation} label="How to Reach" value={place.how_to_reach} />
              <InfoRow icon={Clock} label="Opening Times" value={place.opening_times} />
              <InfoRow icon={Ticket} label="Entry Fee" value={place.entry_fee} />
              <InfoRow icon={Calendar} label="Best Time to Visit" value={place.best_time_to_visit} />
              <InfoRow icon={Phone} label="Contact" value={place.contact} />

              {(place.google_map_url || place.wiki_url) && (
                <div className="mt-6 pt-6 border-t border-[#E6E2D8] flex flex-col gap-3">
                  {place.google_map_url && (
                    <a
                      href={place.google_map_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-full text-sm font-semibold border border-[#C65D47] text-[#C65D47] hover:bg-[#C65D47]/10 transition-all text-center"
                    >
                      <MapPin size={16} />
                      View on Google Maps
                    </a>
                  )}
                  {place.wiki_url && (
                    <a
                      href={place.wiki_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-full text-sm font-semibold bg-[#2A5A43] text-white hover:bg-[#204533] transition-all text-center"
                    >
                      <ArrowRight size={16} />
                      Read Wikipedia Article
                    </a>
                  )}
                </div>
              )}
            </div>
          </motion.div>
        </div>
      </section>

      {/* Related Places */}
      {relatedPlaces.length > 0 && (
        <section className="px-6 md:px-12 lg:px-24 py-12 bg-white/50">
          <h2 className="heading-font text-2xl sm:text-3xl font-medium text-[#1A1814] mb-8 tracking-tight">
            Nearby Attractions
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {relatedPlaces.map((p, i) => (
              <PlaceCard key={p.slug} place={p} index={i} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

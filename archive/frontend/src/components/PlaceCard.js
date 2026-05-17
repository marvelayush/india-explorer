import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { MapPin } from 'lucide-react';

export const PlaceCard = ({ place, index = 0 }) => {
  const navigate = useNavigate();

  return (
    <motion.div
      layout
      data-testid={`place-card-${place.slug}`}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{
        y: -6,
        scale: 1.015,
        boxShadow: "0 20px 35px rgba(198, 93, 71, 0.08)",
        borderColor: "rgba(198, 93, 71, 0.25)"
      }}
      whileTap={{ scale: 0.98 }}
      transition={{
        opacity: { duration: 0.4 },
        y: { duration: 0.4 },
        scale: { type: "spring", stiffness: 400, damping: 22 },
        boxShadow: { duration: 0.2 },
        borderColor: { duration: 0.2 },
        layout: { type: "spring", stiffness: 350, damping: 25 }
      }}
      onClick={() => navigate(`/place/${place.slug}`)}
      className="group cursor-pointer rounded-2xl border border-[#E6E2D8] bg-white transition-colors duration-200"
    >
      <div className="img-zoom rounded-t-2xl">
        <img
          src={place.image_url}
          alt={place.name}
          className="w-full h-48 object-cover rounded-t-2xl"
          loading="lazy"
          onError={(e) => {
            e.target.src = 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800&h=600&fit=crop';
          }}
        />
      </div>
      <div className="p-5">
        <span className="text-xs tracking-[0.2em] uppercase font-bold text-[#C65D47]">
          {place.category}
        </span>
        <h3 className="heading-font text-xl font-medium text-[#1A1814] mt-1 mb-2 group-hover:text-[#C65D47] transition-colors">
          {place.name}
        </h3>
        <p className="text-sm text-[#5C564D] leading-relaxed line-clamp-2">
          {place.description}
        </p>
        <div className="flex items-center gap-1.5 mt-3 text-xs text-[#5C564D]">
          <MapPin size={12} />
          <span>{place.best_time_to_visit}</span>
        </div>
      </div>
    </motion.div>
  );
};

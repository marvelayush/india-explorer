import { useState, useCallback, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import indiaMapData from '@svg-maps/india';

// Map package IDs to database slugs
const ID_TO_SLUG = {
  'an': 'andaman-and-nicobar-islands',
  'ap': 'andhra-pradesh',
  'ar': 'arunachal-pradesh',
  'as': 'assam',
  'br': 'bihar',
  'ch': 'chandigarh',
  'ct': 'chhattisgarh',
  'dn': 'dadra-and-nagar-haveli-and-daman-and-diu',
  'dd': 'dadra-and-nagar-haveli-and-daman-and-diu',
  'dl': 'delhi',
  'ga': 'goa',
  'gj': 'gujarat',
  'hr': 'haryana',
  'hp': 'himachal-pradesh',
  'jk': 'jammu-and-kashmir',
  'jh': 'jharkhand',
  'ka': 'karnataka',
  'kl': 'kerala',
  'ld': 'lakshadweep',
  'mp': 'madhya-pradesh',
  'mh': 'maharashtra',
  'mn': 'manipur',
  'ml': 'meghalaya',
  'mz': 'mizoram',
  'nl': 'nagaland',
  'or': 'odisha',
  'py': 'puducherry',
  'pb': 'punjab',
  'rj': 'rajasthan',
  'sk': 'sikkim',
  'tn': 'tamil-nadu',
  'tg': 'telangana',
  'tr': 'tripura',
  'up': 'uttar-pradesh',
  'ut': 'uttarakhand',
  'wb': 'west-bengal',
};

// Region assignments for coloring
const ID_TO_REGION = {
  'jk': 'north', 'hp': 'north', 'pb': 'north', 'hr': 'north', 'dl': 'north', 'ch': 'north', 'ut': 'north',
  'rj': 'west', 'gj': 'west', 'ga': 'west', 'dn': 'west', 'dd': 'west',
  'up': 'central', 'mp': 'central', 'ct': 'central',
  'br': 'east', 'jh': 'east', 'wb': 'east', 'or': 'east',
  'mh': 'south', 'tg': 'south', 'ap': 'south', 'ka': 'south', 'kl': 'south', 'tn': 'south', 'py': 'south',
  'sk': 'northeast', 'ar': 'northeast', 'as': 'northeast', 'ml': 'northeast', 'nl': 'northeast', 'mn': 'northeast', 'mz': 'northeast', 'tr': 'northeast',
  'an': 'island', 'ld': 'island',
};

const REGION_FILLS = {
  north: '#EACDB7',
  west: '#D9BFCC',
  central: '#B8D4B8',
  east: '#B5C9DD',
  south: '#E8D9A8',
  northeast: '#C9BED6',
  island: '#A8CDDD',
};

const REGION_LABELS = {
  north: 'North',
  west: 'West',
  central: 'Central',
  east: 'East',
  south: 'South',
  northeast: 'Northeast',
  island: 'Islands',
};

export const IndiaMap = () => {
  const [hovered, setHovered] = useState(null);
  const [tooltipPos, setTooltipPos] = useState({ x: 0, y: 0 });
  const svgRef = useRef(null);
  const navigate = useNavigate();
  const [isTouch, setIsTouch] = useState(false);

  useEffect(() => {
    setIsTouch(window.matchMedia("(hover: none)").matches);
  }, []);

  const handleMouseMove = useCallback((e) => {
    if (isTouch || !svgRef.current) return;
    const rect = svgRef.current.getBoundingClientRect();
    setTooltipPos({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top - 40,
    });
  }, [isTouch]);

  const handleStateClick = (e, locationId, slug) => {
    // Dynamically update tooltip position on touch/click so it aligns perfectly
    if (svgRef.current) {
      const rect = svgRef.current.getBoundingClientRect();
      setTooltipPos({
        x: e.clientX - rect.left,
        y: e.clientY - rect.top - 40,
      });
    }

    if (isTouch) {
      if (hovered === locationId) {
        if (slug) navigate(`/state/${slug}`);
      } else {
        setHovered(locationId);
      }
    } else {
      if (slug) navigate(`/state/${slug}`);
    }
  };

  const hoveredLocation = indiaMapData.locations.find(l => l.id === hovered);

  return (
    <div className="relative w-full max-w-[620px] mx-auto" data-testid="india-map-svg">
      {/* Map container with subtle shadow */}
      <div className="relative rounded-3xl overflow-hidden bg-[#F4F0EA] p-4 md:p-6 border border-[#E6E2D8] shadow-[0_4px_40px_rgba(0,0,0,0.06)]">
        {/* Map title */}
        <div className="text-center mb-3">
          <h3 className="heading-font text-lg font-medium text-[#1A1814]">Political Map of India</h3>
          <p className="text-xs text-[#5C564D]">
            {isTouch ? 'Tap once to highlight, tap again to explore' : 'Move cursor across states and click to explore'}
          </p>
        </div>

        <svg
          ref={svgRef}
          viewBox={indiaMapData.viewBox}
          className="w-full h-auto select-none"
          onMouseMove={handleMouseMove}
          onClick={(e) => {
            // Click outside a state clears any touch selection
            if (e.target === e.currentTarget || e.target.tagName === 'rect') {
              setHovered(null);
            }
          }}
          role="img"
          aria-label="Interactive political map of India"
        >
          {/* Saffron Sizzling Red Glow Outline Filter */}
          <defs>
            <filter id="red-glow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="2" stdDeviation="4" floodColor="#E53E3E" floodOpacity="0.65" />
            </filter>
          </defs>

          {/* Ocean/background */}
          <rect x="0" y="0" width="612" height="696" fill="#F4F0EA" />

          {/* State paths */}
          {indiaMapData.locations.map((location) => {
            const region = ID_TO_REGION[location.id] || 'central';
            const isHovered = hovered === location.id;
            const slug = ID_TO_SLUG[location.id];

            return (
              <path
                key={location.id}
                data-testid={`state-path-${slug || location.id}`}
                d={location.path}
                fill={isHovered ? '#E53E3E' : REGION_FILLS[region]}
                stroke={isHovered ? '#C53030' : '#8B8477'}
                strokeWidth={isHovered ? '1.5' : '0.5'}
                strokeLinejoin="round"
                filter={isHovered ? 'url(#red-glow)' : 'none'}
                style={{
                  cursor: 'pointer',
                  transition: 'fill 0.25s cubic-bezier(0.4, 0, 0.2, 1), stroke-width 0.25s, stroke 0.25s',
                }}
                onMouseEnter={() => !isTouch && setHovered(location.id)}
                onMouseLeave={() => !isTouch && setHovered(null)}
                onClick={(e) => handleStateClick(e, location.id, slug)}
              >
                <title>{location.name}</title>
              </path>
            );
          })}
        </svg>

        {/* Floating Tooltip */}
        <AnimatePresence>
          {hoveredLocation && (
            <motion.div
              initial={{ opacity: 0, y: 8, scale: 0.95 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: 8, scale: 0.95 }}
              transition={{ duration: 0.15, ease: 'easeOut' }}
              className="absolute pointer-events-none z-20"
              style={{ left: tooltipPos.x, top: tooltipPos.y, transform: 'translateX(-50%)' }}
            >
              <div className="bg-[#1A1814] text-white px-3 py-2 rounded-xl shadow-[0_10px_25px_rgba(0,0,0,0.15)] flex flex-col items-center gap-0.5 border border-white/10">
                <div className="flex items-center gap-1.5">
                  <span className="text-sm font-semibold">{hoveredLocation.name}</span>
                  <span className="text-[10px] bg-[#E53E3E] text-white px-1.5 py-0.5 rounded-md font-bold uppercase tracking-wider">
                    {REGION_LABELS[ID_TO_REGION[hoveredLocation.id]] || ''}
                  </span>
                </div>
                <span className="text-[10px] text-white/70 font-semibold tracking-wide">
                  {isTouch ? 'Tap again to explore ➔' : 'Click to explore ➔'}
                </span>
              </div>
              <div className="w-2.5 h-2.5 bg-[#1A1814] rotate-45 mx-auto -mt-1.5 border-r border-b border-white/10" />
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Legend */}
      <div className="flex flex-wrap gap-x-5 gap-y-2 justify-center mt-6">
        {Object.entries(REGION_FILLS).map(([region, color]) => (
          <div key={region} className="flex items-center gap-2">
            <div className="w-3.5 h-3.5 rounded-sm border border-[#8B8477]/30" style={{ backgroundColor: color }} />
            <span className="text-xs text-[#5C564D] font-medium capitalize">{REGION_LABELS[region]}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

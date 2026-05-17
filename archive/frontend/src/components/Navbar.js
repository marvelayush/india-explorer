import { Link, useNavigate } from 'react-router-dom';
import { Search, MapPin, ArrowLeft } from 'lucide-react';

export const Navbar = ({ showBack = false, onSearchClick }) => {
  const navigate = useNavigate();

  return (
    <nav
      data-testid="navbar"
      className="fixed top-0 left-0 right-0 z-50 glass"
    >
      <div className="px-6 md:px-12 lg:px-24 py-4 flex items-center justify-between">
        <div className="flex items-center gap-4">
          {showBack && (
            <button
              data-testid="back-to-map-button"
              onClick={() => navigate(-1)}
              className="p-2 rounded-full hover:bg-[#E6E2D8]/50 transition-colors"
            >
              <ArrowLeft size={20} className="text-[#1A1814]" />
            </button>
          )}
          <Link
            to="/home"
            data-testid="logo-link"
            className="flex items-center gap-2 no-underline"
          >
            <MapPin size={22} className="text-[#C65D47]" />
            <span className="heading-font text-xl md:text-2xl font-semibold text-[#1A1814] tracking-tight">
              India Explorer
            </span>
          </Link>
        </div>
        {onSearchClick && (
          <button
            data-testid="nav-search-button"
            onClick={onSearchClick}
            className="flex items-center gap-2 px-4 py-2 rounded-full border border-[#E6E2D8] hover:bg-white/80 transition-colors text-sm text-[#5C564D]"
          >
            <Search size={16} />
            <span className="hidden sm:inline">Search places...</span>
          </button>
        )}
      </div>
    </nav>
  );
};

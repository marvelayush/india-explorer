import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { ArrowRight } from 'lucide-react';

const BG_IMAGES = [
  "https://images.pexels.com/photos/30638768/pexels-photo-30638768.jpeg?auto=compress&w=800",
  "https://images.unsplash.com/photo-1677868821169-08885cfcb495?w=800&h=600&fit=crop",
  "https://images.pexels.com/photos/35080149/pexels-photo-35080149.jpeg?auto=compress&w=800",
  "https://images.unsplash.com/photo-1723871568974-886dc3351ec3?w=800&h=600&fit=crop",
];

export default function LandingPage() {
  const navigate = useNavigate();

  return (
    <motion.div
      data-testid="landing-page"
      onClick={() => navigate('/home')}
      className="min-h-screen bg-[#1A1814] relative overflow-hidden cursor-pointer flex items-center justify-center grain"
    >
      {/* Background images */}
      <div className="absolute inset-0 pointer-events-none">
        <motion.img
          src={BG_IMAGES[0]}
          alt=""
          initial={{ opacity: 0, scale: 1.1 }}
          animate={{ opacity: 0.12, scale: 1 }}
          transition={{ duration: 2, delay: 0.5 }}
          className="absolute top-0 left-0 w-[45%] h-[50%] object-cover rounded-br-[80px]"
        />
        <motion.img
          src={BG_IMAGES[1]}
          alt=""
          initial={{ opacity: 0, scale: 1.1 }}
          animate={{ opacity: 0.1, scale: 1 }}
          transition={{ duration: 2, delay: 0.8 }}
          className="absolute bottom-0 right-0 w-[40%] h-[45%] object-cover rounded-tl-[80px]"
        />
        <motion.img
          src={BG_IMAGES[2]}
          alt=""
          initial={{ opacity: 0 }}
          animate={{ opacity: 0.08 }}
          transition={{ duration: 2, delay: 1.2 }}
          className="absolute top-[15%] right-[5%] w-[25%] h-[30%] object-cover rounded-3xl"
        />
        <motion.img
          src={BG_IMAGES[3]}
          alt=""
          initial={{ opacity: 0 }}
          animate={{ opacity: 0.08 }}
          transition={{ duration: 2, delay: 1.5 }}
          className="absolute bottom-[10%] left-[8%] w-[22%] h-[28%] object-cover rounded-3xl"
        />
      </div>

      {/* Floating decorative elements */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <motion.div
          animate={{ y: [0, -25, 0], rotate: [0, 5, 0] }}
          transition={{ repeat: Infinity, duration: 8, ease: "easeInOut" }}
          className="absolute top-[20%] left-[10%] w-28 h-28 border border-[#E89A3C]/15 rounded-full"
        />
        <motion.div
          animate={{ y: [0, 20, 0], rotate: [0, -5, 0] }}
          transition={{ repeat: Infinity, duration: 10, ease: "easeInOut" }}
          className="absolute bottom-[25%] right-[12%] w-20 h-20 border border-[#C65D47]/15 rounded-full"
        />
        <motion.div
          animate={{ y: [0, -15, 0] }}
          transition={{ repeat: Infinity, duration: 6, ease: "easeInOut" }}
          className="absolute top-[50%] right-[25%] w-12 h-12 border border-[#E89A3C]/10 rounded-sm rotate-45"
        />
        <motion.div
          animate={{ y: [0, 18, 0] }}
          transition={{ repeat: Infinity, duration: 7, ease: "easeInOut" }}
          className="absolute bottom-[40%] left-[20%] w-16 h-16 border border-[#2A5A43]/15 rounded-sm rotate-12"
        />
        {/* Gradient overlays */}
        <div className="absolute inset-0 bg-gradient-to-b from-[#1A1814]/40 via-transparent to-[#1A1814]/60" />
        <div className="absolute inset-0 bg-gradient-to-r from-[#1A1814]/30 via-transparent to-[#1A1814]/30" />
      </div>

      {/* Main content */}
      <div className="relative z-10 text-center px-6 select-none">
        {/* Overline */}
        <motion.p
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3, duration: 0.8 }}
          className="text-xs tracking-[0.4em] uppercase text-[#E89A3C]/50 mb-4"
        >
          Discover the Beauty of
        </motion.p>

        {/* INDIA */}
        <div className="flex justify-center items-baseline gap-1 md:gap-2">
          {"INDIA".split("").map((letter, i) => (
            <motion.span
              key={`india-${i}`}
              initial={{ opacity: 0, y: 80, rotateX: 90 }}
              animate={{ opacity: 1, y: 0, rotateX: 0 }}
              transition={{ duration: 1, delay: 0.5 + i * 0.12, ease: [0.22, 1, 0.36, 1] }}
              className="heading-font text-7xl sm:text-8xl md:text-[10rem] lg:text-[13rem] font-medium text-[#E89A3C] inline-block leading-none"
              style={{ textShadow: '0 0 80px rgba(232,154,60,0.15)' }}
            >
              {letter}
            </motion.span>
          ))}
        </div>

        {/* EXPLORER */}
        <div className="flex justify-center items-baseline gap-0.5 md:gap-1 -mt-2 md:-mt-4">
          {"EXPLORER".split("").map((letter, i) => (
            <motion.span
              key={`explorer-${i}`}
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 1.2 + i * 0.06, ease: [0.22, 1, 0.36, 1] }}
              className="heading-font text-2xl sm:text-3xl md:text-5xl lg:text-6xl font-light text-white/85 inline-block tracking-[0.3em] md:tracking-[0.4em]"
            >
              {letter}
            </motion.span>
          ))}
        </div>

        {/* Decorative divider */}
        <motion.div
          initial={{ scaleX: 0 }}
          animate={{ scaleX: 1 }}
          transition={{ duration: 1, delay: 2 }}
          className="h-[1px] bg-gradient-to-r from-transparent via-[#E89A3C]/40 to-transparent w-52 md:w-72 mx-auto my-6 md:my-8"
        />

        {/* By Ayush Narayan */}
        <motion.p
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 2.3, duration: 0.8 }}
          className="text-sm md:text-base text-[#E89A3C]/50 tracking-[0.25em] uppercase"
          style={{ fontFamily: 'var(--font-body)' }}
        >
          By Ayush Narayan
        </motion.p>

        {/* CTA */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 3 }}
          className="mt-14 md:mt-20"
        >
          <motion.div
            animate={{ opacity: [0.4, 0.8, 0.4] }}
            transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
            className="inline-flex items-center gap-3 px-6 py-3 rounded-full border border-white/10"
          >
            <span className="text-xs md:text-sm tracking-wider text-white/40 uppercase">
              Click anywhere to begin your journey
            </span>
            <motion.div animate={{ x: [0, 8, 0] }} transition={{ repeat: Infinity, duration: 1.5, ease: "easeInOut" }}>
              <ArrowRight size={14} className="text-[#E89A3C]/60" />
            </motion.div>
          </motion.div>
        </motion.div>
      </div>
    </motion.div>
  );
}

import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "@/pages/LandingPage";
import HomePage from "@/pages/HomePage";
import StatePage from "@/pages/StatePage";
import PlacePage from "@/pages/PlacePage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/state/:slug" element={<StatePage />} />
        <Route path="/place/:slug" element={<PlacePage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

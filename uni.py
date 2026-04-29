<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>India University Portal - Anime Nature Study Theme</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    @keyframes fallLeaf {
      0% {
        transform: translateY(-100px) translateX(0) rotateZ(0deg);
        opacity: 1;
      }
      50% {
        opacity: 0.8;
      }
      100% {
        transform: translateY(800px) translateX(100px) rotateZ(360deg);
        opacity: 0;
      }
    }

    @keyframes flowingWater {
      0% {
        background-position: 0% 0%;
      }
      100% {
        background-position: 100% 100%;
      }
    }

    @keyframes floatingBubble {
      0% {
        transform: translateY(0) translateX(0);
        opacity: 0;
      }
      10% {
        opacity: 0.5;
      }
      90% {
        opacity: 0.5;
      }
      100% {
        transform: translateY(-500px) translateX(50px);
        opacity: 0;
      }
    }

    @keyframes gentleGlow {
      0%, 100% {
        box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
      }
      50% {
        box-shadow: 0 0 40px rgba(76, 175, 80, 0.6);
      }
    }

    @keyframes slideInTask {
      from {
        transform: translateX(-30px);
        opacity: 0;
      }
      to {
        transform: translateX(0);
        opacity: 1;
      }
    }

    body {
      background: linear-gradient(135deg, #0f1419 0%, #1a2332 50%, #0d2818 100%);
      color: #e0e0e0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      min-height: 100vh;
      position: relative;
      overflow-x: hidden;
    }

    .background-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      pointer-events: none;
    }

    .water-wave {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 200%;
      height: 120px;
      background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120"><defs><linearGradient id="wave" x1="0%25" y1="0%25" x2="100%25" y2="0%25"><stop offset="0%25" style="stop-color:%231b5e20;stop-opacity:0.2" /><stop offset="50%25" style="stop-color:%234caf50;stop-opacity:0.15" /><stop offset="100%25" style="stop-color:%231b5e20;stop-opacity:0.2" /></linearGradient></defs><path fill="url(%23wave)" d="M0,60 Q300,20 600,60 T1200,60 L1200,120 L0,120 Z"/></svg>') repeat-x;
      animation: flowingWater 12s linear infinite;
      opacity: 0.6;
    }

    .falling-leaf {
      position: absolute;
      width: 30px;
      height: 30px;
      opacity: 0;
      pointer-events: none;
    }

    .leaf {
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 30% 30%, #81c784, #4caf50, #2e7d32);
      clip-path: polygon(50% 0%, 100% 25%, 85% 100%, 50% 85%, 15% 100%, 0% 25%);
      animation: fallLeaf 8s linear forwards;
    }

    .floating-bubble {
      position: absolute;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, rgba(129, 199, 132, 0.3), rgba(76, 175, 80, 0.1));
      border: 1px solid rgba(129, 199, 132, 0.4);
      animation: floatingBubble 15s ease-in infinite;
    }

    .container {
      position: relative;
      z-index: 10;
      max-width: 1400px;
      margin: 0 auto;
      padding: 2rem;
      min-height: 100vh;
    }

    .header {
      margin-bottom: 2rem;
      animation: slideInTask 0.8s ease-out;
    }

    .header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }

    .header h1 {
      font-size: 2.2rem;
      color: #81c784;
      margin: 0;
      text-shadow: 0 4px 12px rgba(129, 199, 132, 0.2);
      letter-spacing: 1px;
    }

    .header p {
      color: #90caf9;
      font-size: 0.9rem;
      opacity: 0.9;
      margin: 0.3rem 0 0 0;
    }

    .filter-controls {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 12px;
      margin-bottom: 2rem;
      animation: slideInTask 0.8s ease-out 0.2s both;
    }

    .filter-group {
      display: flex;
      flex-direction: column;
    }

    .filter-label {
      font-size: 0.85rem;
      font-weight: 500;
      color: #81c784;
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .filter-input, .filter-select {
      padding: 10px 12px;
      font-size: 13px;
      border: 0.5px solid rgba(129, 199, 132, 0.3);
      background: linear-gradient(135deg, rgba(30, 30, 35, 0.6), rgba(25, 40, 50, 0.6));
      color: #e0e0e0;
      border-radius: 10px;
      backdrop-filter: blur(10px);
      transition: all 0.3s ease;
    }

    .filter-input:focus, .filter-select:focus {
      outline: none;
      border-color: rgba(129, 199, 132, 0.6);
      box-shadow: 0 0 20px rgba(76, 175, 80, 0.2);
    }

    .stats-bar {
      display: flex;
      gap: 2rem;
      margin-bottom: 2rem;
      padding: 1rem;
      background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(33, 150, 243, 0.05) 100%);
      border: 1px solid rgba(129, 199, 132, 0.2);
      border-radius: 12px;
      backdrop-filter: blur(10px);
      animation: slideInTask 0.8s ease-out 0.3s both;
    }

    .stat-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .stat-label {
      color: #90caf9;
      font-size: 0.85rem;
    }

    .stat-value {
      color: #81c784;
      font-weight: 600;
    }

    .university-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .university-card {
      background: linear-gradient(135deg, rgba(30, 30, 35, 0.8) 0%, rgba(25, 40, 50, 0.8) 100%);
      border: 1px solid rgba(129, 199, 132, 0.2);
      border-radius: 16px;
      padding: 1.5rem;
      backdrop-filter: blur(15px);
      animation: slideInTask 0.6s ease-out;
      animation-fill-mode: both;
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .university-card:hover {
      transform: translateY(-8px);
      border-color: rgba(129, 199, 132, 0.6);
      box-shadow: 0 12px 40px rgba(76, 175, 80, 0.25);
      background: linear-gradient(135deg, rgba(40, 40, 45, 0.9) 0%, rgba(35, 50, 60, 0.9) 100%);
    }

    .university-card:nth-child(1) { animation-delay: 0.1s; }
    .university-card:nth-child(2) { animation-delay: 0.15s; }
    .university-card:nth-child(3) { animation-delay: 0.2s; }
    .university-card:nth-child(4) { animation-delay: 0.25s; }
    .university-card:nth-child(5) { animation-delay: 0.3s; }
    .university-card:nth-child(n+6) { animation-delay: 0.35s; }

    .uni-header {
      margin-bottom: 1rem;
    }

    .uni-name {
      font-size: 1.3rem;
      color: #81c784;
      font-weight: 600;
      margin-bottom: 0.3rem;
    }

    .uni-location {
      font-size: 0.85rem;
      color: #90caf9;
      opacity: 0.8;
    }

    .uni-badges {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 1rem;
    }

    .badge {
      font-size: 0.75rem;
      padding: 5px 12px;
      border-radius: 12px;
      font-weight: 600;
      backdrop-filter: blur(10px);
    }

    .badge-type-central {
      background: rgba(76, 175, 80, 0.2);
      color: #81c784;
      border: 0.5px solid rgba(76, 175, 80, 0.4);
    }

    .badge-type-state {
      background: rgba(33, 150, 243, 0.2);
      color: #90caf9;
      border: 0.5px solid rgba(33, 150, 243, 0.4);
    }

    .badge-type-private {
      background: rgba(255, 152, 0, 0.2);
      color: #ffb74d;
      border: 0.5px solid rgba(255, 152, 0, 0.4);
    }

    .badge-type-deemed {
      background: rgba(156, 39, 176, 0.2);
      color: #ce93d8;
      border: 0.5px solid rgba(156, 39, 176, 0.4);
    }

    .badge-stream {
      background: rgba(76, 175, 80, 0.15);
      color: #81c784;
      border: 0.5px solid rgba(76, 175, 80, 0.3);
    }

    .uni-info {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      padding: 1rem;
      background: rgba(0, 0, 0, 0.2);
      border-radius: 10px;
      margin-bottom: 1rem;
    }

    .info-item {
      border-left: 3px solid #4caf50;
      padding-left: 0.8rem;
    }

    .info-label {
      font-size: 0.75rem;
      color: #90caf9;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.3rem;
    }

    .info-value {
      font-size: 0.95rem;
      color: #e0e0e0;
      font-weight: 500;
    }

    .uni-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 1rem;
      border-top: 0.5px solid rgba(129, 199, 132, 0.2);
    }

    .scholarship-badge {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.85rem;
      color: #81c784;
      font-weight: 600;
    }

    .expand-btn {
      background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(33, 150, 243, 0.1));
      border: 0.5px solid rgba(129, 199, 132, 0.4);
      color: #81c784;
      padding: 0.6rem 1.2rem;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.3s ease;
      font-size: 0.85rem;
    }

    .expand-btn:hover {
      background: linear-gradient(135deg, rgba(76, 175, 80, 0.3), rgba(33, 150, 243, 0.15));
      border-color: rgba(129, 199, 132, 0.7);
      transform: translateY(-2px);
      box-shadow: 0 8px 16px rgba(76, 175, 80, 0.2);
    }

    .uni-details {
      display: none;
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 0.5px solid rgba(129, 199, 132, 0.2);
      animation: slideInTask 0.4s ease-out;
    }

    .uni-details.active {
      display: block;
    }

    .details-section {
      margin-bottom: 1.5rem;
    }

    .details-title {
      color: #81c784;
      font-size: 0.95rem;
      font-weight: 600;
      margin-bottom: 0.7rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .section-icon {
      width: 20px;
      height: 20px;
      background: rgba(129, 199, 132, 0.2);
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
    }

    .course-list, .facility-list {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
    }

    .course-badge, .facility-badge {
      background: rgba(76, 175, 80, 0.1);
      border: 0.5px solid rgba(76, 175, 80, 0.3);
      color: #81c784;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-size: 0.8rem;
    }

    .scholarship-list {
      background: rgba(76, 175, 80, 0.05);
      border-left: 3px solid #4caf50;
      padding: 0.8rem;
      border-radius: 6px;
    }

    .scholarship-item {
      font-size: 0.85rem;
      color: #90caf9;
      margin-bottom: 0.5rem;
      line-height: 1.4;
    }

    .scholarship-item strong {
      color: #81c784;
    }

    .contact-info {
      background: rgba(33, 150, 243, 0.05);
      border-left: 3px solid #2196f3;
      padding: 0.8rem;
      border-radius: 6px;
      font-size: 0.85rem;
    }

    .contact-item {
      margin-bottom: 0.6rem;
      color: #90caf9;
    }

    .contact-label {
      color: #81c784;
      font-weight: 600;
    }

    .contact-info a {
      color: #90caf9;
      text-decoration: none;
    }

    .contact-info a:hover {
      color: #81c784;
    }

    .no-results {
      text-align: center;
      padding: 3rem;
      color: #90caf9;
      font-size: 1.1rem;
    }

    @media (max-width: 768px) {
      .university-grid {
        grid-template-columns: 1fr;
      }

      .header h1 {
        font-size: 1.8rem;
      }

      .filter-controls {
        grid-template-columns: 1fr;
      }

      .stats-bar {
        flex-direction: column;
        gap: 1rem;
      }

      .uni-info {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="background-container">
    <div class="water-wave"></div>
    <div id="leaf-container"></div>
    <div id="bubble-container"></div>
  </div>

  <div class="container">
    <div class="header">
      <div class="header-top">
        <div>
          <h1>🌿 India University Portal</h1>
          <p>Discover your perfect academic sanctuary. Find the right university for your journey.</p>
        </div>
      </div>
    </div>

    <div class="filter-controls">
      <div class="filter-group">
        <label class="filter-label">Search University</label>
        <input type="text" id="searchInput" class="filter-input" placeholder="Search by name...">
      </div>
      <div class="filter-group">
        <label class="filter-label">University Type</label>
        <select id="typeFilter" class="filter-select">
          <option value="">All Types</option>
          <option value="Central Government">Central Government</option>
          <option value="State Government">State Government</option>
          <option value="Private">Private</option>
          <option value="Deemed">Deemed</option>
        </select>
      </div>
      <div class="filter-group">
        <label class="filter-label">Stream</label>
        <select id="streamFilter" class="filter-select">
          <option value="">All Streams</option>
          <option value="Engineering">Engineering</option>
          <option value="Science">Science</option>
          <option value="Arts">Arts</option>
          <option value="Commerce">Commerce</option>
          <option value="Medical">Medical</option>
          <option value="Management">Management</option>
          <option value="Law">Law</option>
        </select>
      </div>
      <div class="filter-group">
        <label class="filter-label">State</label>
        <select id="stateFilter" class="filter-select">
          <option value="">All States</option>
          <option value="Delhi">Delhi</option>
          <option value="Maharashtra">Maharashtra</option>
          <option value="Tamil Nadu">Tamil Nadu</option>
          <option value="Karnataka">Karnataka</option>
          <option value="Uttar Pradesh">Uttar Pradesh</option>
          <option value="West Bengal">West Bengal</option>
          <option value="Gujarat">Gujarat</option>
          <option value="Punjab">Punjab</option>
          <option value="Rajasthan">Rajasthan</option>
          <option value="Telangana">Telangana</option>
          <option value="Haryana">Haryana</option>
          <option value="Odisha">Odisha</option>
        </select>
      </div>
    </div>

    <div class="stats-bar">
      <div class="stat-item">
        <span class="stat-label">Total Universities:</span>
        <span class="stat-value" id="totalCount">0</span>
      </div>
      <div class="stat-item">
        <span class="stat-label">Filtered Results:</span>
        <span class="stat-value" id="filteredCount">0</span>
      </div>
      <div class="stat-item">
        <span class="stat-label">Scholarships Available:</span>
        <span class="stat-value" id="scholarshipCount">0</span>
      </div>
    </div>

    <div id="universityList" class="university-grid">
    </div>

    <div id="noResults" class="no-results" style="display: none;">
      No universities found matching your criteria. Try adjusting your filters.
    </div>
  </div>

  <script>
    const universities = [
      { id: 1, name: "IIT Bombay", state: "Maharashtra", type: "Central Government", stream: "Engineering", cutoff: "AIR 1-500", fee: "₹1,80,000/yr", contact: { phone: "+91-22-2576 7000", email: "admissions@iitb.ac.in", website: "iitb.ac.in", address: "Powai, Mumbai" }, courses: ["B.Tech CSE", "B.Tech Mechanical", "B.Tech ECE", "M.Tech", "PhD"], hostel: { capacity: "3500 students", fee: "₹10,000-15,000/yr", facilities: ["AC/Non-AC Rooms", "Mess", "WiFi", "Gym", "Sports Complex"] }, scholarship: { available: true, types: ["Merit-based: 20-30% seats", "SC/ST: Govt support", "OBC: Govt support"], maxAmount: "Full tuition" } },
      { id: 2, name: "IIT Delhi", state: "Delhi", type: "Central Government", stream: "Engineering", cutoff: "AIR 1-500", fee: "₹1,80,000/yr", contact: { phone: "+91-11-2659 1000", email: "admissions@iitd.ac.in", website: "iitd.ac.in", address: "Hauz Khas, Delhi" }, courses: ["B.Tech CSE", "B.Tech ECE", "B.Tech Civil", "M.Tech", "MBA", "PhD"], hostel: { capacity: "3200 students", fee: "₹12,000-18,000/yr", facilities: ["Single/Double Rooms", "Mess", "WiFi", "Swimming Pool"] }, scholarship: { available: true, types: ["Merit-based", "SC/ST/OBC support", "Innovation grants"], maxAmount: "Full tuition" } },
      { id: 3, name: "IIT Madras", state: "Tamil Nadu", type: "Central Government", stream: "Engineering", cutoff: "AIR 1-500", fee: "₹1,80,000/yr", contact: { phone: "+91-44-2257 8293", email: "admissions@iitm.ac.in", website: "iitm.ac.in", address: "Chennai" }, courses: ["B.Tech CSE", "B.Tech Mechanical", "B.Tech Chemical", "M.Tech", "PhD"], hostel: { capacity: "3800 students", fee: "₹10,000-15,000/yr", facilities: ["AC/Non-AC", "Mess", "WiFi", "Gym", "Sports"] }, scholarship: { available: true, types: ["Merit: ₹50000/sem", "SC/ST: Full support", "National scholarship"], maxAmount: "₹1,20,000/yr" } },
      { id: 4, name: "Delhi University", state: "Delhi", type: "Central Government", stream: "Arts", cutoff: "85-95 percentile", fee: "₹50,000-80,000/yr", contact: { phone: "+91-11-2766 6659", email: "admissions@du.ac.in", website: "du.ac.in", address: "North Campus, Delhi" }, courses: ["B.A (History)", "B.A (Economics)", "B.A (Political Science)", "M.A", "PhD"], hostel: { capacity: "5000 students", fee: "₹8,000-12,000/yr", facilities: ["Multiple hostels", "Common Mess", "WiFi", "Sports"] }, scholarship: { available: true, types: ["Free Studentship (merit)", "SC/ST: Full tuition", "OBC: ₹50,000/yr"], maxAmount: "Full tuition" } },
      { id: 5, name: "JNU", state: "Delhi", type: "Central Government", stream: "Arts", cutoff: "80-92 percentile", fee: "₹35,000-60,000/yr", contact: { phone: "+91-11-2670 4421", email: "admissions@jnu.ac.in", website: "jnu.ac.in", address: "New Delhi" }, courses: ["B.A (Sociology)", "B.A (International Studies)", "M.A", "PhD"], hostel: { capacity: "4500 students", fee: "₹5,000-10,000/yr", facilities: ["Subsidized hostels", "Common Mess", "WiFi"] }, scholarship: { available: true, types: ["Govt grant: ₹40000/yr", "SC/ST: Full waiver", "TA Fellowship"], maxAmount: "₹1,00,000/yr" } },
      { id: 6, name: "BHU", state: "Uttar Pradesh", type: "Central Government", stream: "Science", cutoff: "82-90 percentile", fee: "₹60,000-95,000/yr", contact: { phone: "+91-542-2368 201", email: "admissions@bhu.ac.in", website: "bhu.ac.in", address: "Varanasi" }, courses: ["B.Sc (Physics)", "B.Sc (Chemistry)", "B.Sc (Biology)", "M.Sc", "PhD"], hostel: { capacity: "8000 students", fee: "₹10,000-16,000/yr", facilities: ["Multiple hostels", "Mess", "WiFi", "Medical center"] }, scholarship: { available: true, types: ["Merit: ₹60000/sem", "SC/ST: Full support", "Research fellowship"], maxAmount: "₹1,60,000/yr" } },
      { id: 7, name: "NIT Trichy", state: "Tamil Nadu", type: "Central Government", stream: "Engineering", cutoff: "AIR 5000-8000", fee: "₹1,05,000/yr", contact: { phone: "+91-431-2500 1000", email: "admissions@nitt.edu", website: "nitt.edu", address: "Tiruchirappalli" }, courses: ["B.Tech CSE", "B.Tech ECE", "B.Tech Civil", "M.Tech", "MBA", "PhD"], hostel: { capacity: "2500 students", fee: "₹8,000-12,000/yr", facilities: ["Hostel blocks", "Mess", "WiFi", "Sports"] }, scholarship: { available: true, types: ["Govt scholarship: ₹40000/sem", "SC/ST: Full tuition"], maxAmount: "Full tuition" } },
      { id: 8, name: "BITS Pilani", state: "Rajasthan", type: "Private", stream: "Engineering", cutoff: "280-340/400", fee: "₹1,80,000-2,50,000/yr", contact: { phone: "+91-1596-242 042", email: "admission@pilani.bits-pilani.ac.in", website: "bits-pilani.ac.in", address: "Pilani" }, courses: ["B.E CSE", "B.E ECE", "B.E Mechanical", "M.Tech", "Integrated M.Tech", "PhD"], hostel: { capacity: "2500 students", fee: "₹80,000-120,000/yr", facilities: ["Fully AC Rooms", "WiFi", "Multi-cuisine Mess", "Gym", "Cinema"] }, scholarship: { available: true, types: ["Merit: ₹1,50,000/yr", "Leadership award: ₹2,00,000"], maxAmount: "Full tuition" } },
      { id: 9, name: "AIIMS Delhi", state: "Delhi", type: "Central Government", stream: "Medical", cutoff: "99 percentile", fee: "₹60,000/yr", contact: { phone: "+91-11-2659 3567", email: "admission@aiims.edu", website: "aiims.edu", address: "Ansari Nagar, Delhi" }, courses: ["MBBS", "BDS", "M.D", "M.S", "PhD"], hostel: { capacity: "800 students", fee: "₹15,000-20,000/yr", facilities: ["AC Rooms", "Food court", "WiFi", "Hospital access"] }, scholarship: { available: true, types: ["Govt support: ₹50000/yr", "SC/ST: Full support", "Research stipend"], maxAmount: "Full tuition" } },
      { id: 10, name: "IIM Ahmedabad", state: "Gujarat", type: "Central Government", stream: "Management", cutoff: "98+ percentile", fee: "₹8,00,000 (2 yrs)", contact: { phone: "+91-79-3985 3000", email: "admissions@iima.ac.in", website: "iima.ac.in", address: "Vastrapur, Ahmedabad" }, courses: ["MBA (2-yr)", "Executive MBA", "Fellow Programme", "PhD"], hostel: { capacity: "600 students", fee: "₹80,000-100,000/yr", facilities: ["Spacious rooms", "Food court", "WiFi", "Gym"] }, scholarship: { available: true, types: ["Merit: ₹2,00,000/sem", "Financial aid available"], maxAmount: "₹4,00,000" } },
      { id: 11, name: "Ashoka University", state: "Haryana", type: "Private", stream: "Arts", cutoff: "88-96 percentile", fee: "₹1,50,000-2,50,000/yr", contact: { phone: "+91-130-410 2000", email: "admissions@ashoka.edu.in", website: "ashoka.edu.in", address: "Sonipat" }, courses: ["B.A (Economics)", "B.A (Psychology)", "B.A (History)", "M.A", "Executive"], hostel: { capacity: "1500 students", fee: "₹1,50,000-2,00,000/yr", facilities: ["Luxury AC rooms", "International cuisine", "Counseling", "Gym"] }, scholarship: { available: true, types: ["Need-based: up to 80%", "Merit: ₹50,000-100,000/yr"], maxAmount: "Full tuition" } },
      { id: 12, name: "Mumbai University", state: "Maharashtra", type: "State Government", stream: "Arts", cutoff: "80-88 percentile", fee: "₹50,000-85,000/yr", contact: { phone: "+91-22-2240 3000", email: "admissions@mu.ac.in", website: "mu.ac.in", address: "Mumbai" }, courses: ["B.A (Economics)", "B.A (History)", "B.A (Political Science)", "M.A", "PhD"], hostel: { capacity: "2000 students", fee: "₹10,000-15,000/yr", facilities: ["Hostels", "Mess", "WiFi"] }, scholarship: { available: true, types: ["Post-Matric: ₹30,000/yr", "Merit-based: ₹20,000/yr"], maxAmount: "₹50,000/yr" } },
      { id: 13, name: "NIT Rourkela", state: "Odisha", type: "Central Government", stream: "Engineering", cutoff: "AIR 7000-10000", fee: "₹1,05,000/yr", contact: { phone: "+91-661-246 2200", email: "admissions@nitrkl.ac.in", website: "nitrkl.ac.in", address: "Rourkela" }, courses: ["B.Tech CSE", "B.Tech Mechanical", "B.Tech Metallurgy", "M.Tech", "PhD"], hostel: { capacity: "2800 students", fee: "₹8,000-12,000/yr", facilities: ["Multiple hostels", "Mess", "WiFi", "Sports"] }, scholarship: { available: true, types: ["Merit: ₹35000/sem", "SC/ST: Full support"], maxAmount: "Full tuition" } },
      { id: 14, name: "FLAME University", state: "Maharashtra", type: "Private", stream: "Arts", cutoff: "82-92 percentile", fee: "₹1,20,000-1,80,000/yr", contact: { phone: "+91-212-607 0000", email: "admissions@flame.edu.in", website: "flame.edu.in", address: "Pune" }, courses: ["B.B.A", "B.Com", "B.A (Economics)", "M.A", "Executive"], hostel: { capacity: "1200 students", fee: "₹1,00,000-1,50,000/yr", facilities: ["Modern rooms", "Multi-cuisine food", "WiFi", "Gym", "Sports"] }, scholarship: { available: true, types: ["Merit: ₹75,000/yr", "Need-based: up to 60%"], maxAmount: "Full tuition" } },
      { id: 15, name: "VIT Vellore", state: "Tamil Nadu", type: "Private", stream: "Engineering", cutoff: "Merit-based", fee: "₹2,20,000-2,80,000/yr", contact: { phone: "+91-416-224 2500", email: "admissions@vit.ac.in", website: "vit.ac.in", address: "Vellore" }, courses: ["B.Tech", "B.C.A", "M.Tech", "M.B.A", "PhD"], hostel: { capacity: "4000 students", fee: "₹1,40,000-1,90,000/yr", facilities: ["AC hostels", "WiFi", "Mess", "Gym", "Sports"] }, scholarship: { available: true, types: ["Merit: ₹80,000/yr", "Sports: ₹1,50,000"], maxAmount: "Full tuition" } },
    ];

    function getTypeBadgeClass(type) {
      const mapping = {
        "Central Government": "badge-type-central",
        "State Government": "badge-type-state",
        "Private": "badge-type-private",
        "Deemed": "badge-type-deemed"
      };
      return mapping[type] || "badge-type-central";
    }

    function createUniversityCard(uni) {
      return `
        <div class="university-card">
          <div class="uni-header">
            <div class="uni-name">${uni.name}</div>
            <div class="uni-location">📍 ${uni.state}</div>
          </div>

          <div class="uni-badges">
            <span class="badge ${getTypeBadgeClass(uni.type)}">${uni.type}</span>
            <span class="badge badge-stream">${uni.stream}</span>
            ${uni.scholarship.available ? '<span class="badge badge-stream">💰 Scholarships</span>' : ''}
          </div>

          <div class="uni-info">
            <div class="info-item">
              <div class="info-label">Cutoff</div>
              <div class="info-value">${uni.cutoff}</div>
            </div>
            <div class="info-item">
              <div class="info-label">Annual Fee</div>
              <div class="info-value">${uni.fee}</div>
            </div>
            <div class="info-item">
              <div class="info-label">Courses</div>
              <div class="info-value">${uni.courses.length}+ Programs</div>
            </div>
            <div class="info-item">
              <div class="info-label">Hostel Fee</div>
              <div class="info-value">${uni.hostel.fee}</div>
            </div>
          </div>

          <div class="uni-footer">
            <div class="scholarship-badge">
              ${uni.scholarship.available ? '✓ Scholarships Available' : 'Limited Aid'}
            </div>
            <button class="expand-btn" onclick="toggleDetails(${uni.id})">Details</button>
          </div>

          <div id="details-${uni.id}" class="uni-details">
            <!-- Courses Section -->
            <div class="details-section">
              <div class="details-title">
                <div class="section-icon">📚</div>
                Courses Offered
              </div>
              <div class="course-list">
                ${uni.courses.map(course => `<span class="course-badge">${course}</span>`).join('')}
              </div>
            </div>

            <!-- Scholarship Section -->
            <div class="details-section">
              <div class="details-title">
                <div class="section-icon">💚</div>
                Scholarship Information
              </div>
              <div class="scholarship-list">
                <div class="scholarship-item"><strong>Maximum Benefit:</strong> ${uni.scholarship.maxAmount}</div>
                ${uni.scholarship.types.map(type => `<div class="scholarship-item">• ${type}</div>`).join('')}
              </div>
            </div>

            <!-- Hostel Section -->
            <div class="details-section">
              <div class="details-title">
                <div class="section-icon">🏠</div>
                Hostel Details
              </div>
              <div class="scholarship-list">
                <div class="scholarship-item"><strong>Capacity:</strong> ${uni.hostel.capacity}</div>
                <div class="scholarship-item"><strong>Fee/Year:</strong> ${uni.hostel.fee}</div>
                <div class="scholarship-item" style="margin-top: 0.5rem;"><strong>Amenities:</strong></div>
                <div class="facility-list" style="margin-top: 0.5rem;">
                  ${uni.hostel.facilities.map(fac => `<span class="facility-badge">✓ ${fac}</span>`).join('')}
                </div>
              </div>
            </div>

            <!-- Contact Section -->
            <div class="details-section">
              <div class="details-title">
                <div class="section-icon">📞</div>
                Contact Information
              </div>
              <div class="contact-info">
                <div class="contact-item"><span class="contact-label">Phone:</span> ${uni.contact.phone}</div>
                <div class="contact-item"><span class="contact-label">Email:</span> ${uni.contact.email}</div>
                <div class="contact-item"><span class="contact-label">Address:</span> ${uni.contact.address}</div>
                <div class="contact-item"><span class="contact-label">Website:</span> <a href="https://${uni.contact.website}" target="_blank">${uni.contact.website}</a></div>
              </div>
            </div>
          </div>
        </div>
      `;
    }

    function toggleDetails(id) {
      const details = document.getElementById(`details-${id}`);
      details.classList.toggle('active');
    }

    function filterUniversities() {
      const searchTerm = document.getElementById("searchInput").value.toLowerCase();
      const typeFilter = document.getElementById("typeFilter").value;
      const streamFilter = document.getElementById("streamFilter").value;
      const stateFilter = document.getElementById("stateFilter").value;
      
      const filtered = universities.filter(uni => {
        const matchesSearch = uni.name.toLowerCase().includes(searchTerm) || uni.state.toLowerCase().includes(searchTerm);
        const matchesType = !typeFilter || uni.type === typeFilter;
        const matchesStream = !streamFilter || uni.stream === streamFilter;
        const matchesState = !stateFilter || uni.state === stateFilter;
        return matchesSearch && matchesType && matchesStream && matchesState;
      });
      
      const list = document.getElementById("universityList");
      const noResults = document.getElementById("noResults");
      const totalCount = document.getElementById("totalCount");
      const filteredCount = document.getElementById("filteredCount");
      const scholarshipCount = document.getElementById("scholarshipCount");
      
      totalCount.textContent = universities.length;
      filteredCount.textContent = filtered.length;
      scholarshipCount.textContent = filtered.filter(u => u.scholarship.available).length;
      
      if (filtered.length === 0) {
        list.innerHTML = "";
        noResults.style.display = "block";
      } else {
        noResults.style.display = "none";
        list.innerHTML = filtered.map(uni => createUniversityCard(uni)).join("");
      }
    }

    document.getElementById("searchInput").addEventListener("keyup", filterUniversities);
    document.getElementById("typeFilter").addEventListener("change", filterUniversities);
    document.getElementById("streamFilter").addEventListener("change", filterUniversities);
    document.getElementById("stateFilter").addEventListener("change", filterUniversities);

    // Animation functions for nature elements
    function createFallingLeaf() {
      const container = document.getElementById('leaf-container');
      if (!container) return;
      
      const leaf = document.createElement('div');
      leaf.className = 'falling-leaf';
      
      const startX = Math.random() * window.innerWidth;
      const delay = Math.random() * 3;
      const duration = 8 + Math.random() * 4;
      
      leaf.style.left = startX + 'px';
      leaf.style.top = '-50px';
      leaf.style.animationDuration = duration + 's';
      leaf.style.animationDelay = delay + 's';
      
      leaf.innerHTML = '<div class="leaf"></div>';
      container.appendChild(leaf);
      
      setTimeout(() => leaf.remove(), (duration + delay) * 1000);
    }

    function createFloatingBubble() {
      const container = document.getElementById('bubble-container');
      if (!container) return;
      
      const bubble = document.createElement('div');
      bubble.className = 'floating-bubble';
      
      const size = 20 + Math.random() * 40;
      const startX = Math.random() * window.innerWidth;
      const startY = window.innerHeight + 50;
      const duration = 12 + Math.random() * 8;
      const delay = Math.random() * 4;
      
      bubble.style.width = size + 'px';
      bubble.style.height = size + 'px';
      bubble.style.left = startX + 'px';
      bubble.style.top = startY + 'px';
      bubble.style.animationDuration = duration + 's';
      bubble.style.animationDelay = delay + 's';
      
      container.appendChild(bubble);
      
      setTimeout(() => bubble.remove(), (duration + delay) * 1000);
    }

    setInterval(createFallingLeaf, 2000);
    setInterval(createFloatingBubble, 3000);

    createFallingLeaf();
    createFloatingBubble();

    filterUniversities();
  </script>
</body>
</html>

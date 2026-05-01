import streamlit as st
import streamlit.components.v1 as components
import json
import random

# Configure the Streamlit page
st.set_page_config(page_title="India University Portal", layout="wide")

# Automatically generate the university data in memory and cache it so it loads instantly
@st.cache_data
def get_universities_data():
    states = ["Delhi", "Maharashtra", "Tamil Nadu", "Karnataka", "Uttar Pradesh", "West Bengal", "Gujarat", "Punjab", "Rajasthan", "Telangana", "Haryana", "Odisha"]
    streams = ["Engineering", "Science", "Arts", "Commerce", "Medical", "Management", "Law"]
    types = ["Central Government", "State Government", "Private", "Deemed"]
    
    courses_dict = {
        "Engineering": ["B.Tech CSE", "B.Tech ECE", "B.Tech Civil", "B.Tech Mech", "M.Tech", "PhD"],
        "Science": ["B.Sc Physics", "B.Sc Chemistry", "B.Sc Bio", "M.Sc", "PhD"],
        "Arts": ["B.A History", "B.A Economics", "B.A Political Science", "M.A", "PhD"],
        "Commerce": ["B.Com", "B.Com Hons", "M.Com", "PhD"],
        "Medical": ["MBBS", "BDS", "MD", "MS", "BAMS"],
        "Management": ["BBA", "MBA", "Executive MBA", "PhD"],
        "Law": ["BA LLB", "LLB", "LLM", "PhD"]
    }
    
    facilities = ["AC/Non-AC Rooms", "Mess", "WiFi", "Gym", "Sports Complex", "Library", "Swimming Pool", "Laundromat"]
    merit_types = ["Merit-based", "SC/ST/OBC support", "EWS quota", "Sports Quota", "Defense Quota"]
    
    universities = []
    for i in range(1, 1201):
        state = random.choice(states)
        stream = random.choice(streams)
        type_ = random.choice(types)
        city = state if state == "Delhi" else f"{state} City {random.randint(1, 20)}"
        
        if type_ == "Central Government":
            if stream == "Engineering":
                name = f"NIT {city}" if random.random() > 0.4 else f"IIT {city}"
            elif stream == "Medical":
                name = f"AIIMS {city}"
            elif stream == "Management":
                name = f"IIM {city}"
            elif stream == "Law":
                name = f"NLU {city}"
            else:
                name = f"Central University of {state} ({city})"
        elif type_ == "State Government":
            name = f"State College of {stream}, {city}"
        elif type_ == "Private":
            name = f"Global {stream} Institute, {city}"
        else:
            name = f"Academy of Higher Education, {city}"
            
        name = f"{name} Campus {random.randint(1, 5)}"
        num_courses = random.randint(2, len(courses_dict[stream]))
        
        # Adding explicit cutoffs for CUET, IIT JEE, and NEET
        if type_ == "Central Government" and stream == "Engineering":
            cutoff = f"IIT JEE Advanced AIR {random.randint(100, 5000)}"
        elif stream == "Medical":
            cutoff = f"NEET AIR {random.randint(100, 5000)}"
        else:
            cutoff = f"CUET Score {random.randint(600, 800)}"

        uni = {
            "id": i,
            "name": name,
            "state": state,
            "type": type_,
            "stream": stream,
            "cutoff": cutoff,
            "fee": f"₹{random.randint(40, 500)},000/yr",
            "contact": {
                "phone": f"+91-{random.randint(11, 99)}-{random.randint(1000, 9999)} {random.randint(1000, 9999)}",
                "email": f"info@uni{i}.edu.in",
                "website": f"uni{i}.edu.in",
                "address": f"University Campus Road, {city}, {state}"
            },
            "courses": random.sample(courses_dict[stream], k=num_courses),
            "hostel": {
                "capacity": f"{random.randint(300, 8000)} students",
                "fee": f"₹{random.randint(10, 150)},000/yr",
                "facilities": random.sample(facilities, k=random.randint(2, 6))
            },
            "scholarship": {
                "available": random.random() > 0.25,
                "types": random.sample(merit_types, k=random.randint(1, 3)),
                "maxAmount": f"₹{random.randint(20, 200)},000/yr" if random.random() > 0.5 else "Full tuition"
            }
        }
        universities.append(uni)
    return json.dumps(universities)

universities_data_json = get_universities_data()

html_content = """
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
      0% { transform: translateY(-100px) translateX(0) rotateZ(0deg); opacity: 1; }
      50% { opacity: 0.8; }
      100% { transform: translateY(800px) translateX(100px) rotateZ(360deg); opacity: 0; }
    }

    @keyframes flowingWater {
      0% { background-position: 0% 0%; }
      100% { background-position: 100% 100%; }
    }

    @keyframes floatingBubble {
      0% { transform: translateY(0) translateX(0); opacity: 0; }
      10% { opacity: 0.5; }
      90% { opacity: 0.5; }
      100% { transform: translateY(-500px) translateX(50px); opacity: 0; }
    }

    @keyframes slideInTask {
      from { transform: translateX(-30px); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
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

    .filter-group { display: flex; flex-direction: column; }
    .filter-label {
      font-size: 0.85rem; font-weight: 500; color: #81c784; margin-bottom: 6px;
      text-transform: uppercase; letter-spacing: 0.5px;
    }

    .filter-input, .filter-select {
      padding: 10px 12px; font-size: 13px;
      border: 0.5px solid rgba(129, 199, 132, 0.3);
      background: linear-gradient(135deg, rgba(30, 30, 35, 0.6), rgba(25, 40, 50, 0.6));
      color: #e0e0e0; border-radius: 10px;
      backdrop-filter: blur(10px); transition: all 0.3s ease;
    }

    .filter-input:focus, .filter-select:focus {
      outline: none; border-color: rgba(129, 199, 132, 0.6);
      box-shadow: 0 0 20px rgba(76, 175, 80, 0.2);
    }

    .stats-bar {
      display: flex; gap: 2rem; margin-bottom: 2rem; padding: 1rem;
      background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(33, 150, 243, 0.05) 100%);
      border: 1px solid rgba(129, 199, 132, 0.2); border-radius: 12px;
      backdrop-filter: blur(10px); animation: slideInTask 0.8s ease-out 0.3s both;
    }
    .stat-item { display: flex; align-items: center; gap: 0.5rem; }
    .stat-label { color: #90caf9; font-size: 0.85rem; }
    .stat-value { color: #81c784; font-weight: 600; }

    .lazy-observer { height: 20px; margin-top: 20px; width: 100%; }

    .university-grid {
      display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 1.5rem; margin-bottom: 2rem;
    }

    .university-card {
      background: linear-gradient(135deg, rgba(30, 30, 35, 0.8) 0%, rgba(25, 40, 50, 0.8) 100%);
      border: 1px solid rgba(129, 199, 132, 0.2); border-radius: 16px;
      padding: 1.5rem; backdrop-filter: blur(15px);
      animation: slideInTask 0.6s ease-out; animation-fill-mode: both;
      transition: all 0.3s ease;
    }

    .university-card:hover {
      transform: translateY(-8px); border-color: rgba(129, 199, 132, 0.6);
      box-shadow: 0 12px 40px rgba(76, 175, 80, 0.25);
      background: linear-gradient(135deg, rgba(40, 40, 45, 0.9) 0%, rgba(35, 50, 60, 0.9) 100%);
    }

    .uni-header { margin-bottom: 1rem; }
    .uni-name { font-size: 1.3rem; color: #81c784; font-weight: 600; margin-bottom: 0.3rem; }
    .uni-location { font-size: 0.85rem; color: #90caf9; opacity: 0.8; }
    .uni-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 1rem; }
    .badge { font-size: 0.75rem; padding: 5px 12px; border-radius: 12px; font-weight: 600; backdrop-filter: blur(10px); }
    .badge-type-central { background: rgba(76, 175, 80, 0.2); color: #81c784; border: 0.5px solid rgba(76, 175, 80, 0.4); }
    .badge-type-state { background: rgba(33, 150, 243, 0.2); color: #90caf9; border: 0.5px solid rgba(33, 150, 243, 0.4); }
    .badge-type-private { background: rgba(255, 152, 0, 0.2); color: #ffb74d; border: 0.5px solid rgba(255, 152, 0, 0.4); }
    .badge-type-deemed { background: rgba(156, 39, 176, 0.2); color: #ce93d8; border: 0.5px solid rgba(156, 39, 176, 0.4); }
    .badge-stream { background: rgba(76, 175, 80, 0.15); color: #81c784; border: 0.5px solid rgba(76, 175, 80, 0.3); }

    .uni-info {
      display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;
      padding: 1rem; background: rgba(0, 0, 0, 0.2); border-radius: 10px; margin-bottom: 1rem;
    }
    .info-item { border-left: 3px solid #4caf50; padding-left: 0.8rem; }
    .info-label { font-size: 0.75rem; color: #90caf9; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 0.3rem; }
    .info-value { font-size: 0.95rem; color: #e0e0e0; font-weight: 500; }
    
    .uni-footer {
      display: flex; justify-content: space-between; align-items: center;
      padding-top: 1rem; border-top: 0.5px solid rgba(129, 199, 132, 0.2);
    }
    .scholarship-badge { display: flex; align-items: center; gap: 0.4rem; font-size: 0.85rem; color: #81c784; font-weight: 600; }
    .expand-btn {
      background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(33, 150, 243, 0.1));
      border: 0.5px solid rgba(129, 199, 132, 0.4); color: #81c784;
      padding: 0.6rem 1.2rem; border-radius: 8px; cursor: pointer;
      font-weight: 600; transition: all 0.3s ease; font-size: 0.85rem;
    }
    .expand-btn:hover { background: linear-gradient(135deg, rgba(76, 175, 80, 0.3), rgba(33, 150, 243, 0.15)); border-color: rgba(129, 199, 132, 0.7); transform: translateY(-2px); }

    .uni-details {
      display: none; margin-top: 1rem; padding-top: 1rem;
      border-top: 0.5px solid rgba(129, 199, 132, 0.2); animation: slideInTask 0.4s ease-out;
    }
    .uni-details.active { display: block; }
    .details-section { margin-bottom: 1.5rem; }
    .details-title { color: #81c784; font-size: 0.95rem; font-weight: 600; margin-bottom: 0.7rem; display: flex; align-items: center; gap: 0.5rem; }
    .section-icon { width: 20px; height: 20px; background: rgba(129, 199, 132, 0.2); border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; }
    .course-list, .facility-list { display: flex; flex-wrap: wrap; gap: 0.6rem; }
    .course-badge, .facility-badge { background: rgba(76, 175, 80, 0.1); border: 0.5px solid rgba(76, 175, 80, 0.3); color: #81c784; padding: 0.4rem 0.8rem; border-radius: 6px; font-size: 0.8rem; }
    
    .scholarship-list { background: rgba(76, 175, 80, 0.05); border-left: 3px solid #4caf50; padding: 0.8rem; border-radius: 6px; }
    .scholarship-item { font-size: 0.85rem; color: #90caf9; margin-bottom: 0.5rem; line-height: 1.4; }
    .scholarship-item strong { color: #81c784; }
    
    .contact-info { background: rgba(33, 150, 243, 0.05); border-left: 3px solid #2196f3; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem; }
    .contact-item { margin-bottom: 0.6rem; color: #90caf9; }
    .contact-label { color: #81c784; font-weight: 600; }
    .contact-info a { color: #90caf9; text-decoration: none; }

    .no-results { text-align: center; padding: 3rem; color: #90caf9; font-size: 1.1rem; }
    .pagination-info { text-align: center; color: #90caf9; margin-top: 1rem; font-size: 0.9rem; }
    
    @media (max-width: 768px) {
      .university-grid { grid-template-columns: 1fr; }
      .filter-controls { grid-template-columns: 1fr; }
      .stats-bar { flex-direction: column; gap: 1rem; }
      .uni-info { grid-template-columns: 1fr; }
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
      <h1>🌿 India University Portal</h1>
      <p>Discover your perfect academic sanctuary. Find the right university for your journey.</p>
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
        </select>
      </div>
    </div>

    <div class="stats-bar">
      <div class="stat-item"><span class="stat-label">Total Universities:</span> <span class="stat-value" id="totalCount">0</span></div>
      <div class="stat-item"><span class="stat-label">Filtered Results:</span> <span class="stat-value" id="filteredCount">0</span></div>
      <div class="stat-item"><span class="stat-label">Scholarships Available:</span> <span class="stat-value" id="scholarshipCount">0</span></div>
    </div>

    <div id="universityList" class="university-grid"></div>
    <div id="lazyLoader" class="lazy-observer"></div>
    <div id="paginationInfo" class="pagination-info"></div>

    <div id="noResults" class="no-results" style="display: none;">
      No universities found matching your criteria. Try adjusting your filters.
    </div>
  </div>

  <script>
    const universities = ___UNIVERSITIES_DATA___;
    let currentFiltered = [];
    let itemsDisplayed = 0;
    const ITEMS_PER_PAGE = 30;

    function getTypeBadgeClass(type) {
      const mapping = { "Central Government": "badge-type-central", "State Government": "badge-type-state", "Private": "badge-type-private", "Deemed": "badge-type-deemed" };
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
            <div class="info-item"><div class="info-label">Cutoff</div><div class="info-value">${uni.cutoff}</div></div>
            <div class="info-item"><div class="info-label">Annual Fee</div><div class="info-value">${uni.fee}</div></div>
            <div class="info-item"><div class="info-label">Courses</div><div class="info-value">${uni.courses.length}+ Programs</div></div>
            <div class="info-item"><div class="info-label">Hostel Fee</div><div class="info-value">${uni.hostel.fee}</div></div>
          </div>
          <div class="uni-footer">
            <div class="scholarship-badge">${uni.scholarship.available ? '✓ Scholarships Available' : 'Limited Aid'}</div>
            <button class="expand-btn" onclick="toggleDetails(${uni.id})">Details</button>
          </div>
          <div id="details-${uni.id}" class="uni-details">
            <div class="details-section">
              <div class="details-title"><div class="section-icon">📚</div>Courses Offered</div>
              <div class="course-list">${uni.courses.map(course => `<span class="course-badge">${course}</span>`).join('')}</div>
            </div>
            <div class="details-section">
              <div class="details-title"><div class="section-icon">💚</div>Scholarship Information</div>
              <div class="scholarship-list">
                <div class="scholarship-item"><strong>Maximum Benefit:</strong> ${uni.scholarship.maxAmount}</div>
                ${uni.scholarship.types.map(type => `<div class="scholarship-item">• ${type}</div>`).join('')}
              </div>
            </div>
            <div class="details-section">
              <div class="details-title"><div class="section-icon">🏠</div>Hostel Details</div>
              <div class="scholarship-list">
                <div class="scholarship-item"><strong>Capacity:</strong> ${uni.hostel.capacity}</div>
                <div class="scholarship-item"><strong>Fee/Year:</strong> ${uni.hostel.fee}</div>
                <div class="facility-list" style="margin-top: 0.5rem;">${uni.hostel.facilities.map(fac => `<span class="facility-badge">✓ ${fac}</span>`).join('')}</div>
              </div>
            </div>
            <div class="details-section">
              <div class="details-title"><div class="section-icon">📞</div>Contact Information</div>
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

    window.toggleDetails = function(id) { document.getElementById(`details-${id}`).classList.toggle('active'); };

    function renderMoreItems() {
      const list = document.getElementById("universityList");
      const nextBatch = currentFiltered.slice(itemsDisplayed, itemsDisplayed + ITEMS_PER_PAGE);
      if(nextBatch.length > 0) {
        list.innerHTML += nextBatch.map(createUniversityCard).join("");
        itemsDisplayed += nextBatch.length;
        document.getElementById("paginationInfo").innerText = `Showing ${itemsDisplayed} of ${currentFiltered.length} items`;
      }
    }

    function filterUniversities() {
      const searchTerm = document.getElementById("searchInput").value.toLowerCase();
      const typeFilter = document.getElementById("typeFilter").value;
      const streamFilter = document.getElementById("streamFilter").value;
      const stateFilter = document.getElementById("stateFilter").value;
      
      currentFiltered = universities.filter(uni => {
        return (uni.name.toLowerCase().includes(searchTerm) || uni.state.toLowerCase().includes(searchTerm)) &&
               (!typeFilter || uni.type === typeFilter) &&
               (!streamFilter || uni.stream === streamFilter) &&
               (!stateFilter || uni.state === stateFilter);
      });
      
      document.getElementById("totalCount").textContent = universities.length;
      document.getElementById("filteredCount").textContent = currentFiltered.length;
      document.getElementById("scholarshipCount").textContent = currentFiltered.filter(u => u.scholarship.available).length;
      
      itemsDisplayed = 0;
      document.getElementById("universityList").innerHTML = "";
      
      if (currentFiltered.length === 0) {
        document.getElementById("noResults").style.display = "block";
        document.getElementById("paginationInfo").innerText = "";
      } else {
        document.getElementById("noResults").style.display = "none";
        renderMoreItems();
      }
    }

    document.getElementById("searchInput").addEventListener("keyup", filterUniversities);
    document.getElementById("typeFilter").addEventListener("change", filterUniversities);
    document.getElementById("streamFilter").addEventListener("change", filterUniversities);
    document.getElementById("stateFilter").addEventListener("change", filterUniversities);

    const observer = new IntersectionObserver((entries) => { if(entries[0].isIntersecting) renderMoreItems(); }, { rootMargin: "100px" });
    observer.observe(document.getElementById("lazyLoader"));

    function createFallingLeaf() {
      const container = document.getElementById('leaf-container');
      if (!container) return;
      const leaf = document.createElement('div'); leaf.className = 'falling-leaf';
      const duration = 8 + Math.random() * 4;
      leaf.style.left = Math.random() * window.innerWidth + 'px';
      leaf.style.top = '-50px';
      leaf.style.animationDuration = duration + 's';
      leaf.innerHTML = '<div class="leaf"></div>';
      container.appendChild(leaf);
      setTimeout(() => leaf.remove(), duration * 1000);
    }
    
    function createFloatingBubble() {
      const container = document.getElementById('bubble-container');
      if (!container) return;
      const bubble = document.createElement('div'); bubble.className = 'floating-bubble';
      const size = 20 + Math.random() * 40; const duration = 12 + Math.random() * 8;
      bubble.style.width = size + 'px'; bubble.style.height = size + 'px';
      bubble.style.left = Math.random() * window.innerWidth + 'px';
      bubble.style.top = window.innerHeight + 50 + 'px';
      bubble.style.animationDuration = duration + 's';
      container.appendChild(bubble);
      setTimeout(() => bubble.remove(), duration * 1000);
    }

    setInterval(createFallingLeaf, 2000);
    setInterval(createFloatingBubble, 3000);
    filterUniversities();
  </script>
</body>
</html>
"""

html_content = html_content.replace('___UNIVERSITIES_DATA___', universities_data_json)

# Inject the HTML/CSS/JS into Streamlit
components.html(html_content, height=1200, scrolling=True)

// Initialize the map
const map = L.map('map').setView([14.2203, 121.004], 10); // Centered on CALABARZON Region with adjusted zoom level

// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Data for provinces: [latitude, longitude, intensity (cases)]
const dengueData = [
    [14.4791, 120.8965, 44169], // Cavite
    [14.2786, 121.4164, 42013], // Laguna
    [13.7565, 121.0583, 28465], // Batangas
    [14.5202, 121.1914, 27686], // Rizal
    [14.0334, 121.7728, 18211], // Quezon
    [13.9348, 121.6179, 2633],  // Lucena City
];

// Create a heatmap layer
const heat = L.heatLayer(dengueData, {
    radius: 25,         // Radius of each "heat" point
    blur: 15,           // Blur effect for the heat
    maxZoom: 10,        // Maximum zoom level for heatmap
    gradient: {         // Custom color gradient
        0.1: '#0172e1',
        0.4: '#0172e1',
        0.7: '#0172e1',
        1.0: '#0172e1'
    }
}).addTo(map);

// Add markers for provinces with popups
const provinces = [
    { name: "Cavite", lat: 14.4791, lng: 120.8965, cases: 44169 },
    { name: "Laguna", lat: 14.2786, lng: 121.4164, cases: 42013 },
    { name: "Batangas", lat: 13.7565, lng: 121.0583, cases: 28465 },
    { name: "Rizal", lat: 14.5202, lng: 121.1914, cases: 27686 },
    { name: "Quezon", lat: 14.0334, lng: 121.7728, cases: 18211 },
    { name: "Lucena City", lat: 13.9348, lng: 121.6179, cases: 2633 }
];

provinces.forEach(province => {
    L.marker([province.lat, province.lng]).addTo(map)
        .bindPopup(`<b>${province.name}</b><br>Dengue Cases: ${province.cases}`);
});
var mymap = L.map('map1').setView([52.23329, 20.99875], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/dark-v10',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYnJhdmVrIiwiYSI6ImNrZ3h5d3B4ZjBvdTIzMHJyZHcxcXRqYngifQ._PaPqzd8rw6rDloG72CxGA'
}).addTo(mymap);
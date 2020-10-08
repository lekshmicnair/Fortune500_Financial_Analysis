// Creating map object
var myMap = L.map("map", {
  center: [37.07, -95.75],
  zoom: 5
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/light-v10",
  accessToken: API_KEY
}).addTo(myMap);



// Assemble API query URL
var url = "http://127.0.0.1:5000/api/map";

// Grab the data with d3
d3.json(url, function(response) {

  console.log(response)
  console.log("Lets build the clusters")
  // Create a new marker cluster group
  var markers = L.markerClusterGroup();
  var arrayObject = Object.values(response);
  
  //Declare the variables
  var lat = arrayObject[5];
  var long = arrayObject[6];
  var title = arrayObject[3];
  var rank = arrayObject[11];
  var profit =arrayObject[10];
  var revenue = arrayObject[13];
  var number_companies= Object.values(arrayObject[3]).length;

// Loop through data
for (var i = 0; i < number_companies; i++) { 
  // Add a new marker to the cluster group and bind a pop-up
  markers.addLayer(L.marker(
  L.latLng(
      (lat[i]),
      (long[i])
    )
  ).bindPopup("Company:"+title[i]+"<br> Rank:"+rank[i]+"<br> Profit($M):"+profit[i]+"<br> Revenue($M):"+revenue[i]));
 
};
  // Add our marker cluster layer to the map
  myMap.addLayer(markers);

});

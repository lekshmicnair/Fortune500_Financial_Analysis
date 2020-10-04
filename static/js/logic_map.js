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

  //d3.request("http://127.0.0.1:5000/api/map").get(response => {
    //console.log(JSON.parse(response.response));


  
  console.log(response)
  console.log("lets build the clusters")
  // Create a new marker cluster group
  var markers = L.markerClusterGroup();
  console.log(Object.keys(response).length);
  
  var arrayObject = Object.values(response);
  console.log (arrayObject);
  //console.log(arrayObject[6])

  //Declare the variables
  var lat = arrayObject[5];
  var long = arrayObject[6];
  var title = arrayObject[3];
  var rank = arrayObject[11];
  var profit =arrayObject[10];
  var revenue = arrayObject[13];
  console.log(long[0]);

// Loop through data
for (var i = 0; i < 500; i++) {
  //console.log(lat[i]);
  //console.log(long[i]);
  
  // Add a new marker to the cluster group and bind a pop-up
  //
  markers.addLayer(L.marker(
  L.latLng(
      (lat[i]),
      (long[i])
    )
  ).bindPopup("Company:"+title[i]+"<br> Rank:"+rank[i]+"<br> Profit($M):"+profit[i]+"<br> Revenue($M):"+revenue[i]));
 // markers.addLayer(L.marker(parseFloat(lat[i]), parseFloat(long[i])).bindPopup(title[i]));
  
}
  // Add our marker cluster layer to the map
  myMap.addLayer(markers);

});

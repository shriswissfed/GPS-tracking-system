var a=11.0183;
var b=76.9625;
var c=10.6700;
var d=77.0200;
var map = L.map('map');

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var control = L.Routing.control({
	waypoints: [
	L.latLng(28.6139,77.2090),
        L.latLng(11.0168,76.9558)
	],
serviceUrl: 'http://router.project-osrm.org/viaroute',
	geocoder: L.Control.Geocoder.nominatim(),
    routeWhileDragging: true,
    reverseWaypoints: true,
    showAlternatives: true,
    show: true,
    altLineOptions: {
        styles: [
            {color: 'black', opacity: 0.15, weight: 9},
            {color: 'white', opacity: 0.8, weight: 6},
            {color: 'blue', opacity: 0.5, weight: 2}
        ]
    }
}).addTo(map);

L.Routing.errorControl(control).addTo(map);

var circle = L.circle([a,b], 1000, {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5
}).addTo(map);

 var routeArray = new Array();
  routeArray = control.getWaypoints();
alert(routeArray[0].latLng.lng);



/*control.on('routingstart', function(e) {
  this.getRouter().route(
    e.waypoints,
    function(err, result) {
      console.log(result[0].summary.totalDistance)
    }
  );
});
*/




/*control.on('routeselected', function(e) {
    var routes = e.route;
    // Do something with the route here
    alert(_routes[0].summary.totalDistance);
});
*/


alert('Distance:'+ control._routes[0].summary.totalDistance);

var i= 0;
control._routes[0].summary.totalDistance =i;

//control.getPlan().setWaypoints({latLng: L.latLng([0, 0])});

var popup = L.popup();
function onMapClick(e) {
popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng)
        .openOn(map);
var lat1=e.latlng.lat;
var lng1=e.latlng.lng;


function onMapClicks(e)
{
	popup
	        .setLatLng(e.latlng)
	        .setContent("You clicked the map at " + e.latlng)
	        .openOn(map);

var lat=e.latlng.lat;
var lng=e.latlng.lng;
var control1 = L.Routing.control({
	waypoints: [
	L.latLng(lat1,lng1),
        L.latLng(lat,lng)
	],
serviceUrl: 'http://router.project-osrm.org/viaroute',
	geocoder: L.Control.Geocoder.nominatim(),
    routeWhileDragging: true,
    reverseWaypoints: true,
    showAlternatives: true,
    altLineOptions: {
        styles: [
            {color: 'black', opacity: 0.15, weight: 9},
            {color: 'white', opacity: 0.8, weight: 6},
            {color: 'blue', opacity: 0.5, weight: 2}
        ]
    }
}).addTo(map);
L.Routing.errorControl(control).addTo(map);


var routeArray1 = new Array();
  routeArray1 = control1.getWaypoints();
alert(routeArray1[0].latLng.lng);

alert('Distance:'+ control1._routes[0].summary.totalDistance);

//control1.getPlan().setWaypoints({latLng: L.latLng([0, 0])});



         }

map.on('click',onMapClicks);


				 }

map.on('click',onMapClick);

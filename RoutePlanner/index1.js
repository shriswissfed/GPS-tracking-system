var map = L.map('map');
var loc ={
    lat1:11.0183,
    lng1:76.9725,

    lat2:10.6700,
    lng2:77.0200,

    lat3:11.0189,
    lng3:76.0234,

    lat4:11.0134,
    lng4:77.9010,

    lat5:11.0144,
    lng5:77.8010,

    lat6:11.0234,
    lng6:77.9020
};
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var control = L.Routing.control({
    waypoints: [
        L.latLng(loc.lat1,loc.lng1),
        L.latLng(loc.lat2,loc.lng2)
    ],
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

alert('Distance:'+ control._routes[0].summary.totalDistance);




var polygon = L.polygon([[loc.lat2,loc.lng2],[loc.lat3,loc.lng3],
[loc.lat1,loc.lng1]
]).addTo(map);


// var control1 = L.Routing.control({
//     waypoints: [
//         L.latLng(loc.lat4,loc.lng4)
//     ],
//     routeWhileDragging: true,
// }).addTo(map);

// map.on('click', function(e) {   // you can trigger the addition of waypoints with events if u want

    var control1 = L.Routing.control({
    waypoints: [
        L.latLng(loc.lat3,loc.lng3),
        L.latLng(loc.lat4,loc.lng4)
        ]
        }).addTo(map);


alert('Distance:'+ control1._routes[1].summary.totalDistance);





     var control2 = L.Routing.control({
    waypoints: [
        L.latLng(loc.lat5,loc.lng5),
        L.latLng(loc.lat6,loc.lng6)
        ]
        }).addTo(map);

alert('Distance:'+ control2._routes[2].summary.totalDistance);




var polygon = L.polygon([
[loc.lat2,loc.lng2],[loc.lat3,loc.lng3],
[loc.lat1,loc.lng1]
]).addTo(mymap);





    //   var control3= L.Routing.control({
    // waypoints: [
    //     L.latLng(loc.lat3,loc.lng3),
    //     L.latLng(loc.lat4,loc.lng4)
    //     ]
    //     }).addTo(map);

// });

//call the controls as you want ...or with some eventlisentning
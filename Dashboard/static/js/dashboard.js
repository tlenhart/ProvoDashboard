// Base javascript file.
var objects;
var transportation_injuries = [];
var percent_ontime = [];
var auto_accidents = [];
var public_ridership = [];
var potholes_filled = [];

//new Morris.Line({
//    element: 'testgraph',
//    data: [
//        {year: '2007', value: '1000'},
//        {year: '2008', value: '200'},
//        {year: '2009', value: '200'},
//        {year: '2010', value: '175'},
//        {year: '2011', value: '250'}
//    ],
//    xkey: 'year',
//    ykeys: ['value'],
//    labels: ['Incidents']
//});
//
//
//new Morris.Line({
//    element: 'testgraph2',
//    data: [
//        {year: '2008', value: '200'},
//        {year: '2009', value: '200'}
//    ],
//    xkey: 'year',
//    ykeys: ['value'],
//    labels: ['Incidents']
//});

//$('#testgraph').addClass("col-md-6");
//$('#testgraph2').addClass("col-md-4");

var transportation_injuries_graph = new Morris.Line({
    element: 'testarea',
    data: [],
    xkey: 'month',
    ykeys: ['value'],
    labels: ['Injuries']
});

var transportation_ontime_graph = new Morris.Line({
    element: 'testarea2',
    data: [],
    xkey: 'month',
    ykeys: ['value'],
    labels: ['% on time']
});

var transportation_autoaccidents_graph = new Morris.Line({
    element: 'testarea3',
    data: [],
    xkey: 'month',
    ykeys: ['value'],
    labels: ['Auto Accidents'],
    lineColors: ['#3ebf33'],
    pointFillColors: ['#7bc143']
});

var transportation_publicridership_graph = new Morris.Bar({
    element: 'testarea4',
    data: [],
    xkey: 'month',
    ykeys: ['value'],
    labels: ['Public Ridership']
});

var transportation_potholes_graph = new Morris.Area({
    element: 'testarea5',
    data: [],
    xkey: 'month',
    ykeys: ['value'],
    labels: ['Potholes Filled']
});

$.get("api/transportation/?format=json&limit=100", function(data) {
    objects = data.objects;

    for (var i = 0; i < objects.length; i++) {
        if (objects[i].category === "Transportation Injuries" || objects[i].category === "Transportation_Injuries")
            transportation_injuries.push({month: generateDate(objects[i].month, objects[i].year), value: objects[i].value});
        else if (objects[i].category === "% ontime" || objects[i].category === "On time Rate")
            percent_ontime.push({month: generateDate(objects[i].month, objects[i].year), value: objects[i].value});
        else if (objects[i].category === "Auto Accidents")
            auto_accidents.push({month: generateDate(objects[i].month, objects[i].year), value: objects[i].value});
        else if (objects[i].category === "Public Ridership (in thousands)" || objects[i].category === "Ridership")
            public_ridership.push({month: generateDate(objects[i].month, objects[i].year), value: objects[i].value});
        else if (objects[i].category === "Potholes Filled (YTD)" || objects[i].category === "Pot holes Filled" || objects[i].category === "Pot Holes Filled (YTD)")
            potholes_filled.push({month: generateDate(objects[i].month, objects[i].year), value: objects[i].value});
    }

    $('.loadergif').hide();

    console.log(transportation_injuries);
    transportation_injuries_graph.setData(transportation_injuries);
    transportation_ontime_graph.setData(percent_ontime);
    transportation_autoaccidents_graph.setData(auto_accidents);
    transportation_publicridership_graph.setData(public_ridership);
    transportation_potholes_graph.setData(potholes_filled);
});

function generateDate (month, year) {
    var rval = year.toString() + "-";
    switch (month) {
        case "January":
            rval += "01";
            break;
        case "February":
            rval += "02";
            break;
        case "March":
            rval += "03";
            break;
        case "April":
            rval += "04";
            break;
        case "May":
            rval += "05";
            break;
        case "June":
            rval += "06";
            break;
        case "July":
            rval += "07";
            break;
        case "August":
            rval += "08";
            break;
        case "September":
            rval += "09";
            break;
        case "October":
            rval += "10";
            break;
        case "November":
            rval += "11";
            break;
        case "December":
            rval += "12";
            break;
        default:
            rval += "12";
    }
    return rval;
}
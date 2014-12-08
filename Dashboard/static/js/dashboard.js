// Base javascript file.
var test;
var testdata = [];

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

var graph = new Morris.Line({
    element: 'testarea',
    data: [],
    xkey: 'month',
    ykeys: ['value'],
    labels: ['Injuries']
});

$.get("api/transportation/?format=json&limit=100", function(data) {
    //console.log(data);
    test = data.objects;
    //$('#testarea').html(test[0].category.toString());

    for (var i = 0; i < 10; i++) {
        if (test[i].category === "Transportation Injuries")
            testdata.push({month: generateDate(test[i].month, test[i].year), value: test[i].value});
    }

    //alert(testdata);
    console.log(testdata);
    graph.setData(testdata);
    //console.log(graphnew.data);
    //console.log(graph.data);
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
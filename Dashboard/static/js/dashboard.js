// Base javascript file.

new Morris.Line({
    element: 'testgraph',
    data: [
        {year: '2007', value: '1000'},
        {year: '2008', value: '200'},
        {year: '2009', value: '200'},
        {year: '2010', value: '175'},
        {year: '2011', value: '250'}
    ],
    xkey: 'year',
    ykeys: ['value'],
    labels: ['Incidents']
});


new Morris.Line({
    element: 'testgraph2',
    data: [
        {year: '2008', value: '200'},
        {year: '2009', value: '200'},
        {year: '2010', value: '175'},
        {year: '2011', value: '250'},
        {year: '2012', value: '455'}
    ],
    xkey: 'year',
    ykeys: ['value'],
    labels: ['Incidents']
});

//$('#testgraph').addClass("col-md-6");
//$('#testgraph2').addClass("col-md-4");
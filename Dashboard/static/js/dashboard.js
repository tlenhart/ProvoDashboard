// Base javascript file.
// Testing minification.

new Morris.Line({
    element: 'testgraph',
    data: [
        {year: '2008', value: '200'},
        {year: '2009', value: '200'},
        {year: '2010', value: '175'},
        {year: '2011', value: '250'}
    ],
    xkey: 'year',
    ykeys: ['value'],
    labels: ['Incidents']
});
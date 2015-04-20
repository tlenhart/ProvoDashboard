// Base javascript file.

// Override chart colors
Chart.defaults.global.colours = [
    { // Green 2 (Provo1)
      fillColor: "rgba(117,190,29,0.2)",
      strokeColor: "rgba(117,190,29,1)",
      pointColor: "rgba(117,190,29,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(117,190,29,0.8)"
    },
    { // Green 3 (Provo2)
      fillColor: "rgba(62,191,51,0.2)",
      strokeColor: "rgba(62,191,51,1)",
      pointColor: "rgba(62,191,51,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(62,191,51,0.8)"
    },
    { // red 229,104,100
      fillColor: "rgba(229,104,100,0.2)",
      strokeColor: "rgba(229,104,100,1)",
      pointColor: "rgba(229,104,100,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(229,104,100,0.8)"
    },
    { // green
      fillColor: "rgba(70,191,189,0.2)",
      strokeColor: "rgba(70,191,189,1)",
      pointColor: "rgba(70,191,189,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(70,191,189,0.8)"
    },
    { // blue 4,163,225
      fillColor: "rgba(4,163,225,0.2)",
      strokeColor: "rgba(4,163,225,1)",
      pointColor: "rgba(4,163,225,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(4,163,225,0.8)"
    },
    { // light grey
      fillColor: "rgba(220,220,220,0.2)",
      strokeColor: "rgba(220,220,220,1)",
      pointColor: "rgba(220,220,220,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(220,220,220,0.8)"
    },
    { // yellow 255,174,19
      fillColor: "rgba(255,174,19,0.2)",
      strokeColor: "rgba(255,174,19,1)",
      pointColor: "rgba(255,174,19,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(255,174,19,0.8)"
    },
    { // grey
      fillColor: "rgba(148,159,177,0.2)",
      strokeColor: "rgba(148,159,177,1)",
      pointColor: "rgba(148,159,177,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(148,159,177,0.8)"
    },
    { // dark grey
      fillColor: "rgba(77,83,96,0.2)",
      strokeColor: "rgba(77,83,96,1)",
      pointColor: "rgba(77,83,96,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(77,83,96,1)"
    }
];

Chart.defaults.global.animation = false;

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
/**
 * Created by Sam Keller on 1/17/2015.
 */

var testVar = "testing deployment bug";

// Only safety has been updated so far for the changes in displaying the graphs.
function graphData(){

}

graphData.prototype = {
    subcategories: {},

    load: function(pageCategory, limit, callback){
        var url = "api/"+pageCategory+"/?format=json&limit=" + limit;
        var that = this;
        $.getJSON(url).done(function(data){
            data.objects.forEach(function(datum){
                if (that.subcategories[datum.category.sub_category] === undefined) {
                    // Create a new subcategory container.
                    that.subcategories[datum.category.sub_category] = {
                        title: datum.category.sub_category,
                        description: datum.category.description,
                        dataPoints: [],
                        chartType: datum.category.chart_type,
                        category: pageCategory
                    };
                }
                // Add the data points for the subcategory.
                that.subcategories[datum.category.sub_category].dataPoints.push({
                    month: datum.month,
                    year: datum.year,
                    value: parseInt(datum.value),
                    pk: datum.pk
                });
            });
            callback();
        });
    }
};

function detailedGraphData() {

}

detailedGraphData.prototype = {

    // 127.0.0.1:8001/api/safety/?category__sub_category=Violent%20Crimes

    load: function(pageCategory, subcategory, limit, callback){
        subcategory = encodeURI(subcategory);
        var url = "api/"+pageCategory+"/?category__sub_category="+subcategory+"&format=json&limit=" + limit;
        var that = this;
        $.getJSON(url).done(function(data){
            data.objects.forEach(function(datum){

                console.log(datum);

                // Needs implementation

                //if (that.subcategories[datum.category.sub_category] === undefined) {
                //    // Create a new subcategory container.
                //    that.subcategories[datum.category.sub_category] = {
                //        title: datum.category.sub_category,
                //        description: datum.category.description,
                //        dataPoints: [],
                //        chartType: datum.category.chart_type,
                //        category: pageCategory
                //    };
                //}
                // Add the data points for the subcategory.
                //that.subcategories[datum.category.sub_category].dataPoints.push({
                //    month: datum.month,
                //    year: datum.year,
                //    value: parseInt(datum.value),
                //    pk: datum.pk
                //});
            });
            callback();
        });
    }
};
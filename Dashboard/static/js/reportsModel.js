/**
 * Created by Sam Keller on 1/17/2015.
 */

// Only safety has been updated so far for the changes in displaying the graphs.
function graphData(){

}

graphData.prototype = {
    subcategories: {},

    load: function(department, limit, callback){
        var url = "api/"+department+"/?format=json&limit=" + limit;
        var that = this;
        $.getJSON(url).done(function(data){
            data.objects.forEach(function(datum){
                if (that.subcategories[datum.category.sub_category] === undefined) {
                    // Create a new subcategory container.
                    that.subcategories[datum.category.sub_category] = {
                        title: datum.category.sub_category,
                        description: datum.category.description,
                        dataPoints: [],
                        chartType: datum.category.chart_type
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

function economicData(){

}

economicData.prototype = {
    collections: [],
    category: [],
    month: [],
    value: [],
    year: [],
    pk: [],

    load: function(department, limit, callback){
        var url = "api/"+department+"/?format=json&limit=" + limit;
        var that = this;
        $.getJSON(url).done(function(data){
            that.collections = data.objects;
            that.collections.forEach(function(datum){
                that.category.push(datum.category);
                that.month.push(datum.month);
                that.value.push(datum.value);
                that.year.push(datum.year);
                that.pk.push(datum.pk);
            });
            callback();
        });
    },

    getCategory: function(){
        return this.category;
    },

    getMonth: function(){
        return this.month;
    },

    getValue: function(){
        return this.value;
    },

    getYear: function(){
        return this.year;
    }
};

function civicData(){

}

civicData.prototype = {
    collections: [],
    category: [],
    month: [],
    value: [],
    year: [],
    pk: [],

    load: function(department, limit, callback){
        var url = "api/"+department+"/?format=json&limit=" + limit;
        var that = this;
        $.getJSON(url).done(function(data){
            that.collections = data.objects;
            that.collections.forEach(function(datum){
                that.category.push(datum.category);
                that.month.push(datum.month);
                that.value.push(datum.value);
                that.year.push(datum.year);
                that.pk.push(datum.pk);
            });
            callback();
        });
    },

    getCategory: function(){
        return this.category;
    },

    getMonth: function(){
        return this.month;
    },

    getValue: function(){
        return this.value;
    },

    getYear: function(){
        return this.year;
    }
};

function governmentData(){

}

governmentData.prototype = {
    collections: [],
    category: [],
    month: [],
    value: [],
    year: [],
    pk: [],

    load: function(department, limit, callback){
        var url = "api/"+department+"/?format=json&limit=" + limit;
        var that = this;
        $.getJSON(url).done(function(data){
            that.collections = data.objects;
            that.collections.forEach(function(datum){
                that.category.push(datum.category);
                that.month.push(datum.month);
                that.value.push(datum.value);
                that.year.push(datum.year);
                that.pk.push(datum.pk);
            });
            callback();
        });
    },

    getCategory: function(){
        return this.category;
    },

    getMonth: function(){
        return this.month;
    },

    getValue: function(){
        return this.value;
    },

    getYear: function(){
        return this.year;
    }
};
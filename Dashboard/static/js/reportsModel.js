/**
 * Created by Sam Keller on 1/17/2015.
 */

function transportationData(){

}

transportationData.prototype = {
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

function safetyData(){

}

safetyData.prototype = {
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

function communityData(){

}

communityData.prototype = {
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

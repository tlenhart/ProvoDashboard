/**
 * Created by Todd on 2/26/2015.
 */

var app = angular.module("graphapp", ["chart.js"]);

app.factory('safetyFactory', function($http) {
    //var service = {};
    //
    //var labels = [];
    //var series = ['2014'];
    //var data = [];
    //var options = {};
    //
    //var category = 'safety';
    //var limit = 0;
    //var dataCollection = Object.create(safetyData.prototype);
    //dataCollection.load(category, limit ,function () {
    //    labels = dataCollection.getMonth();
    //    data[0] = dataCollection.getValue();
    //    //$apply();
    //});
    //
    //service.getData = function() {
    //    return category;
    //};
    //
    //return service;
});
var test = {};
app.controller('SafetyController', function($scope/*, safetyFactory*/) {
    $scope.category = 'safety';
    $scope.safetyLoaded = false;
    $scope.limit = 0;
    $scope.dataCollection = {};

    $scope.loadData = function() {
        $scope.dataCollection = Object.create(safetyData.prototype);

        $scope.dataCollection.load($scope.category, $scope.limit ,function () {
            //$scope.labels = $scope.dataCollection.getMonth();
            //$scope.data[0] = $scope.dataCollection.getValue();
            $scope.$apply();
            $scope.safetyLoaded = true;
        });
    };
});

// Data might be duplicated here. (Copies of stuff in SafetyController).
app.controller('GraphController', function($scope) {
    $scope.loaded = false;
    $scope.title = "";
    $scope.description = "";
    $scope.labels = [];
    $scope.series = ['2014'];
    $scope.data = [];
    $scope.values = [];
    $scope.type = '';
    $scope.options = {};
    $scope.onClick = function (points, evt) {
        alert();
    };

    // This might not be the best approach to doing this.
    //  See here: https://stackoverflow.com/questions/14523679/can-you-pass-parameters-to-an-angularjs-controller-on-creation
    $scope.init = function(data) {
        //console.log(data);

        $scope.title = data.title;
        $scope.description = data.description;
        //$scope.chartType = 'pie';
        $scope.chartType = data.chartType;
        //console.log(data.dataPoints);
        data.dataPoints.forEach(function(datum){
            $scope.labels.push(datum.month);
            //$scope.series = ['2014'];
            $scope.values.push(datum.value);
        });

        $scope.charts = ['Line', 'Bar', 'Doughnut', 'Pie', 'Polar Area', 'Radar', 'Base'];
        if ($scope.chartType === "chart-line") {
            $scope.type = 'Line';
            $scope.data[0] = $scope.values;
        }
        else if ($scope.chartType === "chart-bar") {
            $scope.type = 'Bar';
            $scope.data[0] = $scope.values;
        }
        else if ($scope.chartType === "chart-doughnut") {
            $scope.type = 'Doughnut';
            $scope.data = $scope.values;
        }
        else if ($scope.chartType === "chart-pie") {
            $scope.type = 'Pie';
            $scope.data = $scope.values;
        }
        else if ($scope.chartType === "chart-polar") {
            $scope.type = 'PolarArea';
            $scope.data = $scope.values;
        }
        else if ($scope.chartType === "chart-radar") {
            $scope.type = 'Radar';
            $scope.data[0] = $scope.values;
        }
        else {
            $scope.data = $scope.values;
            console.log("Invalid chart type" + $scope.chartType);
            //$scope.values.forEach(function(dp) {
            //   $scope.data.push(parseInt(dp));
            //});
            //$scope.data.push($scope.value);
        }

        //console.log($scope.chartType);

        //console.log($scope.data[0]);
        //console.log($scope.data);
        //console.log($scope.labels);
        //$scope.$apply();

        $('.loadergif').hide();
    };
});
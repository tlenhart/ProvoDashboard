/**
 * Created by Sam Keller on 1/15/2015.
 */

/*
 * Moved stuff from safety.js here. It makes more sense to put it here than to have a
 * different file for each category page.
 */

var app = angular.module("graphapp", ["chart.js", "ui.bootstrap"]);

app.controller('BaseGraphController', function($scope) {
    $scope.category = '';
    //$scope.safetyLoaded = false;
    $scope.limit = 0;
    $scope.dataCollection = {};

    $scope.loadData = function(pageCategory) {
        $scope.category = pageCategory;
        $scope.dataCollection = Object.create(graphData.prototype);

        $scope.dataCollection.load($scope.category, $scope.limit ,function () {
            $scope.$apply();
            //$scope.safetyLoaded = true;
        });
    };
});

// Data might be duplicated here. (Copies of stuff in BaseGraphController). Might be better to store stuff in a factory and pass in a pointer.
app.controller('GraphController', function($scope, $modal) {
    $scope.loaded = false;
    $scope.title = "";
    $scope.description = "";
    $scope.labels = [];
    $scope.series = ['2014'];
    $scope.data = [];
    $scope.values = [];
    $scope.type = '';
    $scope.options = {};
    $scope.colours = Chart.defaults.global.colours;

    $scope.open = function (size) {
        var modalInstance = $modal.open({
            templateUrl: 'modalContent.html',
            controller: 'ModalInstanceCtrl',
            size: size,
            resolve: {
                data: function () {
                    return $scope.data;
                },
                labels: function () {
                    return $scope.labels;
                },
                series: function () {
                    return $scope.series;
                },
                category: function () {
                    return $scope.category;
                },
                type: function () {
                    return $scope.type;
                },
                title: function () {
                    return $scope.title;
                },
                description: function () {
                    return $scope.description;
                }
            }
        });

        modalInstance.result.then(function (){

        });
    };

    // This might not be the best approach to doing this.
    //  See here: https://stackoverflow.com/questions/14523679/can-you-pass-parameters-to-an-angularjs-controller-on-creation
    $scope.init = function(data) {
        $scope.title = data.title;
        $scope.description = data.description;
        $scope.category = data.category;
        $scope.chartType = data.chartType;
        //$scope.colours = ;

        data.dataPoints.forEach(function(datum){
            $scope.labels.push(datum.month);
            //$scope.series = ['2014']; // Should be set to something dynamic/adjustable. Going to have to decide how to do this.
            $scope.values.push(datum.value);
        });

        $scope.charts = ['Line', 'Bar', 'Radar', 'Doughnut', 'Pie', 'PolarArea', 'Base'];
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
            //$scope.data = $scope.values;
            index = Math.floor((Math.random() * 3));
            $scope.type = $scope.charts[index];
            $scope.data[0] = $scope.values;
            console.log("Invalid chart type" + $scope.chartType);
        }

        //console.log($scope.chartType);

        //console.log($scope.data[0]);
        //console.log($scope.data);
        //console.log($scope.labels);
        //$scope.$apply();

        $('.loadergif').hide(); // Might not want or maybe even need this if we end up using ng-cloak.
    };
});

app.controller('ModalInstanceCtrl', function ($scope, $modalInstance, data, labels, series, type, title, description) {
    // This will need to be switched where it grabs new data from the api. (All data perhaps.)
    Chart.defaults.global.animation = true;
    $scope.dataCollection = {};
    $scope.data = data;
    $scope.labels = labels;
    $scope.series = series;
    $scope.type = type;
    $scope.title = title;
    $scope.description = description;

    $scope.$apply();

    $scope.requestData = function() {
        $scope.dataCollection = Object.create(detailedGraphData.prototype);
        $scope.dataCollection.load($scope.category, $scope.limit ,function () {
            //$scope.$apply();
        });
        //$scope.dataCollection.forEach
    };

    $scope.ok = function () {
        $modalInstance.close();
    };

    $scope.close = function() {
        $modalInstance.close();
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    }
});

        //var app = angular.module("graphapp", ["chart.js"]);
        //
        //app.controller("LineCtrl", function ($scope) {
        //    $scope.labels = [];
        //    $scope.series = ['2014'];
        //    $scope.data = [];
        //    $scope.options = {};
        //    $scope.onClick = function (points, evt) {
        //        alert();
        //    };
        //
        //    $scope.initLine = function() {
        //        $scope.category = 'economic';
        //        $scope.limit = 10;
        //        $scope.dataCollection = Object.create(economicData.prototype);
        //        $scope.dataCollection.load($scope.category, $scope.limit ,function () {
        //            $scope.labels = $scope.dataCollection.getMonth();
        //            $scope.data[0] = $scope.dataCollection.getValue();
        //            $scope.$apply();
        //        });
        //        $('.loadergif').hide();
        //    }
        //});
        //
        //app.controller("BarCtrl", function ($scope) {
        //    $scope.labels = [];
        //    $scope.series = ['2014'];
        //    $scope.data = [];
        //    $scope.options = {};
        //    $scope.onClick = function (points, evt) {
        //        alert();
        //    };
        //
        //    $scope.initBar = function() {
        //        $scope.category = 'safety';
        //        $scope.limit = 20;
        //        $scope.dataCollection = Object.create(safetyData.prototype);
        //        $scope.dataCollection.load($scope.category, $scope.limit ,function () {
        //            $scope.labels = $scope.dataCollection.getMonth();
        //            $scope.data[0] = $scope.dataCollection.getValue();
        //            $scope.$apply();
        //        });
        //        $('.loadergif').hide();
        //    }
        //});
        //
        //app.controller("DoughnutCtrl", function ($scope) {
        //    $scope.labels = [];
        //    $scope.series = ['2014'];
        //    $scope.data = [];
        //    $scope.options = {};
        //    $scope.onClick = function (points, evt) {
        //        alert();
        //    };
        //
        //    $scope.initDough = function() {
        //        $scope.category = 'civic';
        //        $scope.limit = 3;
        //        $scope.dataCollection = Object.create(civicData.prototype);
        //        $scope.dataCollection.load($scope.category, $scope.limit ,function () {
        //            $scope.labels = $scope.dataCollection.getMonth();
        //            var i = 0;
        //            $scope.values = $scope.dataCollection.getValue();
        //            for(datum in $scope.values) {
        //                $scope.data[i] = datum;
        //                i++;
        //            }
        //            $scope.$apply();
        //        });
        //        $('.loadergif').hide();
        //    }
        //});
        //
        //app.controller("PolarAreaCtrl", function ($scope) {
        //    $scope.labels = ["Download Sales", "In-Store Sales", "Mail Sales", "Telesales", "Corporate Sales"];
        //    $scope.data = [300, 500, 100, 40, 120];
        //    $scope.onClick = function (points, evt) {
        //        alert("this is where we add the drill down")
        //
        //    };
        //});
        //
        //app.controller("PieCtrl", function ($scope) {
        //    $scope.labels = ["On Time", "Early", "Late"];
        //    $scope.series =["stuff"]
        //    $scope.data = [300, 500, 100];
        //    $scope.onClick = function (points, evt) {
        //        alert("this is where we add the drill down")
        //    };
        //});

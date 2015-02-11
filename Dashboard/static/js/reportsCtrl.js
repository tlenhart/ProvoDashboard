/**
 * Created by Sam Keller on 1/15/2015.
 */

		var app = angular.module("graphapp", ["chart.js"]);

        app.controller("LineCtrl", function ($scope) {
            $scope.labels = [];
            $scope.series = ['2014'];
            $scope.data = [];
            $scope.options = {};
            $scope.onClick = function (points, evt) {
                alert();
            };

            $scope.initLine = function() {
                $scope.category = 'transportation';
                $scope.limit = 10;
                $scope.dataCollection = Object.create(transportationData.prototype);
                $scope.dataCollection.load($scope.category, $scope.limit ,function () {
                    $scope.labels = $scope.dataCollection.getMonth();
                    $scope.data[0] = $scope.dataCollection.getValue();
                    $scope.$apply();
                });
                $('.loadergif').hide();
            }
		});

        app.controller("BarCtrl", function ($scope) {
            $scope.labels = [];
            $scope.series = ['2014'];
            $scope.data = [];
            $scope.options = {};
            $scope.onClick = function (points, evt) {
                alert();
            };

            $scope.initBar = function() {
                $scope.category = 'safety';
                $scope.limit = 20;
                $scope.dataCollection = Object.create(safetyData.prototype);
                $scope.dataCollection.load($scope.category, $scope.limit ,function () {
                    $scope.labels = $scope.dataCollection.getMonth();
                    $scope.data[0] = $scope.dataCollection.getValue();
                    $scope.$apply();
                });
                $('.loadergif').hide();
            }
        });

        app.controller("DoughnutCtrl", function ($scope) {
            $scope.labels = [];
            $scope.series = ['2014'];
            $scope.data = [];
            $scope.options = {};
            $scope.onClick = function (points, evt) {
                alert();
            };

            $scope.initDough = function() {
                $scope.category = 'transportation';
                $scope.limit = 3;
                $scope.dataCollection = Object.create(communityData.prototype);
                $scope.dataCollection.load($scope.category, $scope.limit ,function () {
                    $scope.labels = $scope.dataCollection.getMonth();
                    var i = 0;
                    $scope.values = $scope.dataCollection.getValue();
                    for(datum in $scope.values) {
                        $scope.data[i] = datum;
                        i++;
                    }
                    $scope.$apply();
                });
                $('.loadergif').hide();
            }
        });

        app.controller("PolarAreaCtrl", function ($scope) {
            $scope.labels = ["Download Sales", "In-Store Sales", "Mail Sales", "Telesales", "Corporate Sales"];
            $scope.data = [300, 500, 100, 40, 120];
            $scope.onClick = function (points, evt) {
                alert("this is where we add the drill down")

            };
        });

        app.controller("PieCtrl", function ($scope) {
            $scope.labels = ["On Time", "Early", "Late"];
            $scope.series =["stuff"]
            $scope.data = [300, 500, 100];
            $scope.onClick = function (points, evt) {
                alert("this is where we add the drill down")
            };
        });

/* global angular */
(function() {
  angular.module('app').controller('analyticsCtrl', function($scope, $http, $location, $routeParams) {
          $scope.message = "Hello World";

          $scope.setUp = function() {
            console.log("Setup");
          }

          $scope.data = [
            {
              "date": "June 01, 2016",
              "amount": 100
            },
            {
              "date": "June 02, 2016",
              "amount": 90
            },
            {
              "date": "June 03, 2016",
              "amount": 30
            },
            {
              "date": "June 04, 2016",
              "amount": 140
            },
            {
              "date": "June 05, 2016",
              "amount": 85
            },
            {
              "date": "June 06, 2016",
              "amount": 120
            },
            {
              "date": "June 07, 2016",
              "amount": 75
            },
          ];

          
  })
})();

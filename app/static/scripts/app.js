/* global angular */

(function() {
  var app = angular.module('app',['ngRoute']);

  app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{|');
    $interpolateProvider.endSymbol('|}');

}]);

  app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post = { 'Content-Type' : 'application/x-www-form-urlencoded' };
    $httpProvider.defaults.headers.put = { 'Content-Type' : 'application/x-www-form-urlencoded' };
    $httpProvider.defaults.paramSerializer = '$httpParamSerializerJQLike';
}]);

app.config(function ($anchorScrollProvider) {
    $anchorScrollProvider.disableAutoScrolling();
  });

  app.config(function ($locationProvider) {
      $locationProvider.html5Mode(true);
    })

  app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
            .when('/analytics', { templateUrl: 'analytics',
                                  controller: 'analyticsCtrl'
                                })
            .when('/:id', { templateUrl: 'table',
                            controller: 'categoriesCtrl'
                          })
            // .otherwise('/', { templateUrl: '/categories',
            //                   controller: 'categoriesCtrl'
            //                 });

  }])

})();

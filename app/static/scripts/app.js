/* global angular */

(function() {
  var app = angular.module('app',[]);

  app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{|');
    $interpolateProvider.endSymbol('|}');

}]);

  app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post = { 'Content-Type' : 'application/x-www-form-urlencoded' };
    $httpProvider.defaults.headers.put = { 'Content-Type' : 'application/x-www-form-urlencoded' };
    $httpProvider.defaults.paramSerializer = '$httpParamSerializerJQLike';
}]);

})();

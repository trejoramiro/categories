/* global angular */
(function() {
  angular.module('app').controller('categoriesCtrl', function($scope, $http) {

    $scope.setUp = function() {
      $http.get('/categories/JSON').then(function (response) {
        console.log(response.data.items)
        $scope.items = response.data.items
        $scope.categories = response.data.categories
      })

    };

    $scope.createItem = function(inputName, inputDescription, inputCategory) {
      
      var item = {
        name: inputName,
        description: inputDescription,
        category: inputCategory
      };

      $scope.inputName = "";
      $scope.inputDescription = "";
      $scope.inputCategory = "";

      $scope.items.push(item);
    }

    window.$scope = $scope;
  })
})();

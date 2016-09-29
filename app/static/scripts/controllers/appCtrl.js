/* global angular */
(function() {
  angular.module('app').controller('categoriesCtrl', function($scope, $http, Items) {

    $scope.title = "Recent";
    $scope.editedItem = null;
    $scope.emptyInputFields = true;

    $scope.setUp = function() {
      Items.load().then(function (response) {
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

      $scope.items.push(item);
      $scope.inputName = '';
      $scope.inputDescription = '';
      $scope.inputCategory = '';
      $scope.inputPrice = '';
      $scope.inputImageUrl = '';

      Items.create(item).then(function (response) {
        console.log(response.data);
      })

    }

    $scope.removeItem = function(index) {
      Items.delete(index).then(function(response) {
        $scope.items.splice(index, 1);
        console.log(response.data);
      })
    }

    $scope.changeItems = function(category) {
      Items.find(category).then(function (response) {
        $scope.items = response.data.items;
        $scope.title = category.name;
      })
    }

    $scope.validateInput = function(input) {
      if(input.length > 0) {
        console.debug(input)
      } else {
        console.log("empty")
      }
    }

    $scope.updateItem = function(index) {
      console.log(index);
    }

    $scope.getCategoryName = function(item) {
      for(var i=0; i<$scope.categories; i++) {
        if($scope.categories[i].id === item.categoryId) {
          return $scope.categories[i].name;
      }
      return null;
    }
  }


    window.$scope = $scope;

  })
})();

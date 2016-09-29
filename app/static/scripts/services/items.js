/*global angular */

angular.module('app')
        .factory('Items', function($http, $httpParamSerializerJQLike) {
          return {
            load: function() {
              return $http.get('/categories/JSON');
            },
            find: function(category) {
              var url =  '/categories/'+ category.id + '/JSON';
              return $http.get(url);
            },
            delete: function(index) {
              var item = $scope.items[index];
              var url = '/items/'  + item.id + '/JSON';
              return $http.delete(url);
            },
            create: function(item) {
              return $http({
                  method: 'POST',
                  url: 'items/JSON',
                  data: $httpParamSerializerJQLike(item)
              });
            }
          };
        });

    define(["../angular.min"], function(angular) {

        angular.module('myApp', [])
          .controller('mainController', ['$scope', '$http', function ($scope, $http) {
              $scope.add_person = function(name) {
                    $http.post(
                        'http://127.0.0.1:8080/api/person/',
                        {'name': name}
                    ).then(function(response) {
                        $scope.persons = response.data;
                    });
              }
          }]);

    });

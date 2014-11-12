var app = angular.module('detail.app', []);

app.controller('appController', function($scope, $http) {
    $scope.films=[];
    $http.get('/sscp/list').then(function(result){
            angular.forEach(result, function(object){
                angular.forEach(object, function (value) {
                    $scope.films.push(value);
                });
            });
    });

    $scope.image = {
        'path':'/static/sscp/images/films.png'
    };

    $scope.test = "Hello!";
})

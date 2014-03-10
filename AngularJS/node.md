# Angular JS

### Page by ajax

    :::html
    <html ng-app="phonecatApp">
    <head>
    <script type="text/javascript" src="http://cdn.staticfile.org/angular.js/1.2.0rc3/angular.min.js"></script>
    <script type="text/javascript">
    var phonecatApp = angular.module('phonecatApp', []);
    phonecatApp.controller('TablePagerCtrl', function($scope, $http) {
        $scope.name = "Pageration by http.get";
        $scope.page_no = 0;
        $http.get('/table/next?page_no=' + $scope.page_no).success(function(data) {
            $scope.rows = data.data;
            $scope.page_no++;
        })
        $scope.getNext = function(page_no) {
            if(page_no < 1) {
                page_no = 1;
            }
            $http.get('/table/next?page_no=' + page_no).success(function(data) {
                $scope.rows = data.data;
                $scope.page_no = page_no + 1;
            })
        }
        $scope.getPrev = function(page_no) {
            if(page_no < 2) {
                page_no = 2;
            }
            $http.get('/table/prev?page_no=' + page_no).success(function(data) {
                $scope.rows = data.data;
                $scope.page_no = page_no - 1;
            })
        }
    });
    </script>
    </head>
    <body>
    <div class="row" ng-controller="TablePagerCtrl">
        <div class="col-md-12">
            <legend>{{name}}</legend>
            <table class="table table-bordered">
                <thead>
                    <th>基数</th>
                    <th>阶乘</th>
                </thead>
                <tbody>
                    <tr ng-repeat="row in rows">
                        <td>{{row.index}}</td>
                        <td>{{row.data}}</td>
                    </tr>
                </tbody>
            </table>
            <button class="btn btn-default" ng-click="getPrev(page_no)">Prev</button>
            <button class="btn btn-default" ng-click="getNext(page_no)">Next</button>
        </div>
    </div>
    </body>
    </html>

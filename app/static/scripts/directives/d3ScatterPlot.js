(function () {
angular.module('app.directives', ['d3'])
    .directive('d3Plot', ['d3Service', function(d3Service) {
        return {
            restrict: 'EA',
            scope: {
                data: "=",
                label: "@",
            },
            link: function(scope, element, attrs) {

              scope.render = function(data) {

              var margin = {top: 20, right: 20, bottom: 50, left: 70};
              var width = window.innerWidth;
              var height = window.innerHeight;

              console.log("hello")
              console.log(d3)

              var parseTime = d3.timeParse("%B %d, %Y");
              var x_scale = d3.scaleTime().range([0,width]);
              var y_scale = d3.scaleLinear().range([height,0]);

              var svg = d3.select('#content').append("svg")
                // .attr("viewBox", "0 0 "+width+" "+height)
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                  .attr("transform",
                        "translate(" + margin.left + "," + margin.top + ")");

              x_scale.domain(d3.extent(d3.values(data), function(d) {
                // console.log(parseTime(d.date));
                return parseTime(d.date);
              }));

              y_scale.domain([0, d3.max(d3.values(data), function(d) {
                return d.amount;
              })]);

              svg.append("g")
                .attr("transform", "translate(0," + (height - 1) + ")")
                .attr("class","axis")
                .call(d3.axisBottom(x_scale))

              svg.append("g")
                .attr("class", "axis")
                .call(d3.axisLeft(y_scale));

              svg.selectAll("circle")
                .data(d3.values(data))
                .enter()
                .append("circle")
                .attr("cx", function(d) { console.log(x_scale(parseTime(d.date))); return x_scale(parseTime(d.date))})
                .attr("cy", function(d) { return y_scale(d["amount"])})
                .attr("r", 5);


              };
            }
          };
    }]);

}());

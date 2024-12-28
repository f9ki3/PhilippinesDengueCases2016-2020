$(document).ready(function() {
    $.ajax({
        url: '/get_prediction',
        method: 'GET',
        success: function(response) {
            var casesSeries = response.cases.map(function(value) {
                return parseFloat(value).toFixed(2);
            });
            var deathsSeries = response.deaths.map(function(value) {
                return parseFloat(value).toFixed(2);
            });
            var months = response.month;

            // Calculate the total cases and deaths
            var totalCases = casesSeries.reduce((acc, val) => acc + parseFloat(val), 0).toFixed(2);
            var totalDeaths = deathsSeries.reduce((acc, val) => acc + parseFloat(val), 0).toFixed(2);

            // Append the total cases and deaths to the DOM
            $('#totalCases').text(`${Math.round(totalCases)}`);
            $('#totalDeaths').text(`${Math.round(totalDeaths)}`);

            var options = {
                chart: {
                    type: 'area'
                },
                series: [{
                    name: 'Cases',
                    data: casesSeries,
                    color: '#0172e1' // Updated blue color for cases
                }, {
                    name: 'Deaths',
                    data: deathsSeries,
                    color: '#FF0000' // Red color for deaths
                }],
                xaxis: {
                    categories: months,
                    labels: {
                        style: {
                            colors: '#FFFFFF'
                        }
                    }
                },
                yaxis: {
                    labels: {
                        style: {
                            colors: '#FFFFFF'
                        }
                    }
                },
                title: {
                    text: 'Predicted Dengue Cases and Deaths',
                    style: {
                        color: '#FFFFFF'
                    }
                },
                legend: {
                    position: 'top',
                    labels: {
                        colors: '#FFFFFF'
                    }
                }
            };

            var chart = new ApexCharts(document.querySelector("#chartPrediction"), options);
            chart.render();
        },
        error: function(error) {
            console.log("Error fetching prediction data:", error);
        }
    });
});

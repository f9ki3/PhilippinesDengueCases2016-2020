let barChart; // Declare the chart variable outside the function

function get_dengue_cases(get_dengue) {
    $.ajax({
        url: get_dengue,
        method: 'GET',
        success: function(response) {
            const casesData = response.ph_dengue.cases_series;
            const months = response.ph_dengue.month_series;
            const years = response.ph_dengue.year_series;

            let categories, titleText;

            if (months) {
                categories = months;
                titleText = "Number of Cases by Month";
            } else if (years) {
                categories = years;
                titleText = "Number of Cases from 2016 to 2020";
            } else {
                console.error('No valid time series data found.');
                return;
            }

            // Options for the Bar/Line Chart
            const barChartOptions = {
                chart: {
                    type: "bar", // Change to "line" for a line chart
                    height: 350,
                    toolbar: {
                        show: false // Disable the download or export functionality
                    }
                },
                series: [
                    {
                        name: "Number of Cases",
                        data: casesData
                    }
                ],
                xaxis: {
                    categories: categories, // Months or Years on x-axis
                    title: {
                        text: months ? "Month" : "Year",
                        style: {
                            color: '#ffffff' // Set x-axis title color to white
                        }
                    },
                    labels: {
                        style: {
                            colors: '#ffffff' // Set x-axis labels color to white
                        }
                    }
                },
                yaxis: {
                    title: {
                        text: "Number of Cases",
                        style: {
                            color: '#ffffff' // Set y-axis title color to white
                        }
                    },
                    labels: {
                        style: {
                            colors: '#ffffff' // Set y-axis labels color to white
                        }
                    }
                },
                title: {
                    text: titleText,
                    align: "center",
                    style: {
                        color: '#ffffff' // Set title color to white
                    }
                },
                plotOptions: {
                    bar: {
                        borderRadius: 10 // Add this property to make the bars rounded
                    }
                },
                colors: ['#0172e1'], // Set the bar color to blue
                dataLabels: {
                    enabled: false // Disable data labels inside the chart
                }
            };

            // Destroy the existing chart if it exists
            if (barChart) {
                barChart.destroy();
            }

            // Render the Bar/Line Chart
            barChart = new ApexCharts(document.querySelector("#casesChart"), barChartOptions);
            barChart.render();
        },
        error: function(error) {
            console.error('Error fetching dengue data:', error);
        }
    });
}

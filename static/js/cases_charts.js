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
                        text: months ? "Month" : "Year"
                    }
                },
                yaxis: {
                    title: {
                        text: "Number of Cases"
                    }
                },
                title: {
                    text: titleText,
                    align: "center"
                },
                plotOptions: {
                    bar: {
                        borderRadius: 10 // Add this property to make the bars rounded
                    }
                },
                colors: ['#FF0000'] // Set the bar color to red
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

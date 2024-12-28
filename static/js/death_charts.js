let barChartDeath; // Declare the chart variable outside the function

function get_dengue_death(get_dengue) {
    $.ajax({
        url: get_dengue,
        method: 'GET',
        success: function(response) {
            const casesData = response.ph_dengue.death_series;
            const months = response.ph_dengue.month_series;
            const years = response.ph_dengue.year_series;

            let categories, titleText;

            if (months) {
                categories = months;
                titleText = "Number of Death by Month";
            } else if (years) {
                categories = years;
                titleText = "Number of Death from 2016 to 2020";
            } else {
                console.error('No valid time series data found.');
                return;
            }

            // Options for the Bar/Line Chart
            const barChartDeathOptions = {
                chart: {
                    type: "bar", // Change to "line" for a line chart
                    height: 350,
                    toolbar: {
                        show: false // Disable the toolbar
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
                        text: "Number of Death"
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
                colors: ['#FF0000'], // Set the bar color to red
                dataLabels: {
                    enabled: false // Disable data labels inside the chart
                }
            };

            // Destroy the existing chart if it exists
            if (barChartDeath) {
                barChartDeath.destroy();
            }

            // Render the Bar/Line Chart
            barChartDeath = new ApexCharts(document.querySelector("#deathChart"), barChartDeathOptions);
            barChartDeath.render();
        },
        error: function(error) {
            console.error('Error fetching dengue data:', error);
        }
    });
}

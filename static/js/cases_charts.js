// Options for the Bar/Line Chart (2016-2020 Cases)
const barChartOptions = {
    chart: {
        type: "bar", // Change to "line" for a line chart
        height: 350
    },
    series: [{
        name: "Number of Cases",
        data: [150, 230, 180, 270, 320] // Data for 2016-2020
    }],
    xaxis: {
        categories: ["2016", "2017", "2018", "2019", "2020"], // Years on x-axis
        title: {
            text: "Year"
        }
    },
    yaxis: {
        title: {
            text: "Number of Cases"
        }
    },
    title: {
        text: "Number of Cases from 2016 to 2020",
        align: "center"
    }
};

// Render the Bar/Line Chart
const barChart = new ApexCharts(document.querySelector("#casesChart"), barChartOptions);
barChart.render();


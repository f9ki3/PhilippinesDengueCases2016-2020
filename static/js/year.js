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


// Dummy data for Philippine regions' dengue cases
const heatmapData = [
    { name: "NCR", data: [ { x: "Top Cases", y: 10000 }, { x: "Least Cases", y: 200 } ] },
    { name: "Central Luzon", data: [ { x: "Top Cases", y: 8500 }, { x: "Least Cases", y: 300 } ] },
    { name: "Western Visayas", data: [ { x: "Top Cases", y: 7800 }, { x: "Least Cases", y: 250 } ] },
    { name: "CALABARZON", data: [ { x: "Top Cases", y: 9200 }, { x: "Least Cases", y: 180 } ] },
    { name: "Central Visayas", data: [ { x: "Top Cases", y: 6000 }, { x: "Least Cases", y: 120 } ] }
];

// Options for the Heatmap Chart
const heatmapOptions = {
    chart: {
        type: 'heatmap',
        height: 350
    },
    series: heatmapData,
    title: {
        text: 'Top and Least Dengue Cases by Region'
    },
    xaxis: {
        categories: ["Top Cases", "Least Cases"],
        title: { text: "Case Type" }
    },
    yaxis: {
        title: { text: "Regions" }
    },
    dataLabels: {
        enabled: true,
        style: {
            colors: ["#fff"]
        }
    },
    colors: ["#FF5733", "#2ECC71"], // Red for top cases, Green for least cases
};

// Render the Heatmap Chart
const heatmapChart = new ApexCharts(document.querySelector("#heatmap"), heatmapOptions);
heatmapChart.render();

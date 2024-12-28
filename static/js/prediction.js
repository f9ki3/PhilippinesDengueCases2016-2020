// Include required CDNs in your HTML:
// <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
// <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>

$(document).ready(function () {
    // Fetch preprocessed data from your backend (e.g., Flask API endpoint)
    const apiEndpoint = '/dengue_forecast'; // Replace with your actual API route

    $.getJSON(apiEndpoint, function (data) {
        // Parse the data
        const historicalCases = data.historical_cases;
        const historicalDeaths = data.historical_deaths;
        const forecastCases = data.forecast_cases;
        const forecastDeaths = data.forecast_deaths;
        const percentageDeaths = data.percentage_deaths;

        // Prepare the data for ApexCharts
        const dates = data.dates;
        const casesSeries = [
            {
                name: 'Historical Cases',
                data: historicalCases,
            },
            {
                name: 'Forecast Cases',
                data: forecastCases,
            },
        ];

        const deathsSeries = [
            {
                name: 'Historical Deaths',
                data: historicalDeaths,
            },
            {
                name: 'Forecast Deaths',
                data: forecastDeaths,
            },
        ];

        const percentageSeries = [
            {
                name: 'Percentage of Deaths',
                data: percentageDeaths,
            },
        ];

        // Plot Dengue Cases
        const casesOptions = {
            chart: {
                type: 'line',
                height: 350,
            },
            series: casesSeries,
            xaxis: {
                categories: dates,
            },
            title: {
                text: 'Dengue Cases Forecast',
            },
            yaxis: {
                title: {
                    text: 'Dengue Cases',
                },
            },
        };

        const casesChart = new ApexCharts(document.querySelector("#cases-chart"), casesOptions);
        casesChart.render();

        // Plot Dengue Deaths
        const deathsOptions = {
            chart: {
                type: 'line',
                height: 350,
            },
            series: deathsSeries,
            xaxis: {
                categories: dates,
            },
            title: {
                text: 'Dengue Deaths Forecast',
            },
            yaxis: {
                title: {
                    text: 'Dengue Deaths',
                },
            },
        };

        const deathsChart = new ApexCharts(document.querySelector("#deaths-chart"), deathsOptions);
        deathsChart.render();

        // Plot Percentage of Deaths
        const percentageOptions = {
            chart: {
                type: 'line',
                height: 350,
            },
            series: percentageSeries,
            xaxis: {
                categories: dates,
            },
            title: {
                text: 'Percentage of Deaths Forecast',
            },
            yaxis: {
                title: {
                    text: 'Percentage',
                },
            },
        };

        const percentageChart = new ApexCharts(document.querySelector("#percentage-chart"), percentageOptions);
        percentageChart.render();
    });
});

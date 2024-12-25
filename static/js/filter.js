function config(){
    let filterYear = localStorage.getItem('selectedYear');
    let filterRegion = localStorage.getItem('selectedRegion');

    let queryParams = [];
    if (filterYear) {
        queryParams.push(`year=${filterYear}`);
    }
    if (filterRegion) {
        queryParams.push(`region=${filterRegion}`);
    }

    let get_dengue = '/get_dengue?' + queryParams.join('&');
    let get_dengue_cases_death = '/get_dengue_cases_death?' + queryParams.join('&');
    let get_dengue_most_least = '/get_dengue_most_least?' + queryParams.join('&');
    $.ajax({
        url: get_dengue_cases_death,
        method: 'GET',
        success: function(response) {
            $('#cases').text(response.ph_dengue.total_cases.toLocaleString('en-US'));
            $('#death').text(response.ph_dengue.total_deaths.toLocaleString('en-US'));
        },
        error: function(error) {
            console.error('Error fetching dengue data:', error);
        }
    });
    $.ajax({
        url: get_dengue_most_least,
        method: 'GET',
        success: function(response) {
            $('#mostNo').text(response.most_cases.cases.toLocaleString('en-US'));
            $('#leastNo').text(response.least_cases.cases.toLocaleString('en-US'));
            $('#mostRegion').text("Most Cases" + "(" + response.most_cases.region + ")");
            $('#leastRegion').text("Least Cases" + "(" + response.least_cases.region + ")");
        },
        error: function(error) {
            console.error('Error fetching dengue data:', error);
        }
    });

    console.log(get_dengue);
    console.log(get_dengue_cases_death);
    console.log(get_dengue_most_least);
}

config();
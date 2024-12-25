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

    console.log(get_dengue);
    console.log(get_dengue_cases_death);
    console.log(get_dengue_most_least);
}

config();
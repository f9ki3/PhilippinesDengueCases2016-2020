$(document).ready(function() {
    $.ajax({
        url: '/get_regions',
        method: 'GET',
        success: function(data) {
            data.regions.forEach(function(region) {
                var button = $('<li><a class="dropdown-item">' + region + '</a></li>');
                $('#region-buttons').append(button);
            });
        },
        error: function(error) {
            console.error('Error fetching regions:', error);
        }
    });
});

$(document).on('click', '.dropdown-item', function() {
    var selectedRegion = $(this).text();
    localStorage.setItem('selectedRegion', selectedRegion);
    config()
});
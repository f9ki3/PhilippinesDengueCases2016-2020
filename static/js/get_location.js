$(document).ready(function() {
    $.ajax({
        url: '/get_locations',
        method: 'GET',
        success: function(data) {
            data.locations.forEach(function(region) {
                var button = $('<li><a class="dropdown-item">' + region + '</a></li>');
                $('#location-buttons').append(button);
            });
        },
        error: function(error) {
            console.error('Error fetching regions:', error);
        }
    });

    $(document).on('click', '.dropdown-item', function() {
        var selectedLocation = $(this).text();
        localStorage.setItem('selectedLocation', selectedLocation);
        config();
    });

});
$(document).ready(function() {
    $.ajax({
        url: '/get_years',
        method: 'GET',
        success: function(data) {
            data.years.forEach(function(year) {
                var button = $('<button class="btn bg-accent-blue text-light me-2"></button>').text(year);
                button.on('click', function() {
                    localStorage.setItem('selectedYear', year);
                    config()
                });
                $('#year-buttons').append(button);
            });
        },
        error: function(error) {
            console.error('Error fetching years:', error);
        }
    });
});
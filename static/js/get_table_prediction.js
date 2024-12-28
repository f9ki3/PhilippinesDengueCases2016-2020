$(document).ready(function() {
    $.ajax({
        url: '/get_prediction',
        method: 'GET',
        success: function(data) {
            var tableBody = $('#predictionTableBody');
            tableBody.empty();
            var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
            for (var i = 0; i < data.cases.length; i++) {
                var row = '<tr class="text-light" style="border-top: 1px solid gray">' +
                    '<td class="pt-2 pb-2">' + data.year[i] + '</td>' +
                    '<td class="pt-2 pb-2">' + monthNames[data.month[i] - 1] + '</td>' +
                    '<td class="pt-2 pb-2">' + data.cases[i] + '</td>' +
                    '<td class="pt-2 pb-2">' + data.deaths[i] + '</td>' +
                    '</tr>';
                tableBody.append(row);
            }
        },
        error: function(error) {
            console.log('Error fetching prediction data:', error);
        }
    });
});
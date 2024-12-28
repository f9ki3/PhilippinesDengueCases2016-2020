$('#dashboard-btn').click(function() {
    $('#dashboard').show();
    $('#prediction-div').hide();
    $('#faq-div').hide();
});

$('#prediction-btn').click(function() {
    $('#dashboard').hide();
    $('#prediction-div').show();
    $('#faq').hide();
});

$('#faq-btn').click(function() {
    $('#dashboard').hide();
    $('#predicted').hide();
    $('#faq').show();
});
$('#dashboard-btn').click(function() {
    $('#dashboard').slideDown();
    $('#prediction-div').slideUp();
    $('#faq-div').slideUp();
    $('#dashboard-filter').show();
});

$('#prediction-btn').click(function() {
    $('#dashboard').slideUp();
    $('#prediction-div').slideDown();
    $('#dashboard-filter').hide();
    $('#faq-div').slideUp();
});

$('#faq-btn').click(function() {
    $('#dashboard').slideUp();
    $('#prediction-div').slideUp();
    $('#faq-div').slideDown();
});
function toggleVisibility(showElement, hideElements) {
    $(showElement).slideDown();
    hideElements.forEach(function(element) {
        $(element).slideUp();
    });
}

$('#dashboard-btn').click(function() {
    toggleVisibility('#dashboard', ['#prediction-div', '#faq-div', '#faqs-div']);
    $('#dashboard-filter').show();
    $('#title').show();
    $('#title-faq').hide();
});

$('#prediction-btn').click(function() {
    toggleVisibility('#prediction-div', ['#dashboard', '#faq-div', '#faqs-div']);
    $('#dashboard-filter').hide();
    $('#title').show();
    $('#title-faq').hide();
});

$('#faqs-btn').click(function() {
    toggleVisibility('#faqs-div', ['#dashboard', '#prediction-div']);
    $('#dashboard-filter').hide();
    $('#title').hide();
    $('#title-faq').show();
});

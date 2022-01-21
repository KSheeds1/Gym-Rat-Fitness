/*jshint esversion: 6 */
// Update quantity on click
$('.update').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
});

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('class').split('remove_')[1];
    var url = `/bag/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
    .done(function() {
        location.reload();
    });
});
/*jshint esversion: 6 */
let countrySelected = $('.select-wrapper', 'input.select-dropdown').val();
if(!countrySelected) {
    $('.select-wrapper', 'input.select-dropdown').css('color', '#b8b8b8');
}
$('.select-wrapper', 'input.select-dropdown').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#b8b8b8');
    } else {
        $(this).css('color', '#000');
    }
});
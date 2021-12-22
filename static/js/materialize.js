$(document).ready(function(){
    $(".dropdown-trigger").dropdown({
        coverTrigger: false
    });
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $(".hover").mouseleave(
        function () {
          $(this).removeClass("hover");
        }
    );
    /*Toggle search bar */
    $('#search, .search').on('click', function() {
        $('.search-panel').show("slow");
    });
});
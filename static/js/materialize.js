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
});
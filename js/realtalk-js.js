// jQuery to collapse the navbar on scroll
function sky(){
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
        $(".skyline").addClass("skyline-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
        $(".skyline").removeClass("skyline-collapse");
        console.log("displayed skyline");
    }
}
function divHeight(){
    if ($(window).width() > 767) {
        h1 = $('#how-img-1').css("height");
        h2 = $('#how-img-2').css("height");
        h3 = $('#how-img-3').css("height");
        document.getElementById('how-div-1').style.height = h1;
        document.getElementById('how-div-2').style.height = h2;
        document.getElementById('how-div-3').style.height = h3;
        h1 = $('#chal-img-1').css("height");
        h2 = $('#chal-img-2').css("height");
        document.getElementById('chal-div-1').style.height = h1;
        document.getElementById('chal-div-2').style.height = h2;
    }
    else {
        h1 = $('#how-child-1').css("height");
        h2 = $('#how-child-2').css("height");
        h3 = $('#how-child-3').css("height");
        document.getElementById('how-div-1').style.height = h1;
        document.getElementById('how-div-2').style.height = h2;
        document.getElementById('how-div-3').style.height = h3;
        h1 = $('#chal-child-1').css("height");
        h2 = $('#chal-child-2').css("height");
        document.getElementById('chal-div-1').style.height = h1;
        document.getElementById('chal-div-2').style.height = h2;
    }
}
$(window).scroll(function() {
    sky();
});
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        $('html, body').stop().animate({
            scrollTop: ($($(this).attr('href')).offset().top - 50)
        }, 800, 'easeInOutExpo');
        event.preventDefault();
    });
});
$(function() {
    $('.navbar-collapse ul li a').bind('click', function(event) {
        if ($(window).width() < 768) {
            // Closes the Responsive Menu on Menu Item Click
            $('.navbar-toggle').click();
        }
    });
});
$( window ).on("resize", function() {
    divHeight();
});

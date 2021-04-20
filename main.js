new WOW().init();


$(document).ready(function () {
    new WOW().init();
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        autoplay: true,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    })
});

// Show Or Hide Element Based on ScrollTop
$(document).scroll(function () {
     if ($(document).scrollTop() > 300) {
         $('.top').fadeIn();
     } else {
         $('.top').fadeOut();
     }
 })
 
 $('.top').click(function () {
 
     $('body, html').animate({
         scrollTop: 0
     }, 1500);
 
 })
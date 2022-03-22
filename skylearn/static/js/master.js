// ------------------------------- Home Template JS------------------------------------------------------------------------------------------






jQuery(document).ready(function()
{
	 "use strict"

	 $(".slider").ripples({       //function to get the  ripple water effect
	  dropRadius:12 ,
	  perturbance: 0.01,

});

	 // function to create jQuery typing effect

	var typed = new Typed(".text", {
	  strings:["<strong class='primary'>Welcome, </strong>You are at right place","Start <strong class='primary'>learning</strong>"],

	  typeSpeed:40,
	  backSpeed:30,
	  loop: true
	  // Default value
	});

});





<!-- NO JS VERSION: https://codepen.io/nicolaskadis/full/brQEOd/ -->

$(document).ready(function() {
  var front = document.getElementsByClassName("front");
  var back = document.getElementsByClassName("back");

  var highest = 0;
  var absoluteSide = "";

  for (var i = 0; i < front.length; i++) {
    if (front[i].offsetHeight > back[i].offsetHeight) {
      if (front[i].offsetHeight > highest) {
        highest = front[i].offsetHeight;
        absoluteSide = ".front";
      }
    } else if (back[i].offsetHeight > highest) {
      highest = back[i].offsetHeight;
      absoluteSide = ".back";
    }
  }
  $(".front").css("height", highest);
  $(".back").css("height", highest);
  $(absoluteSide).css("position", "absolute");
});





$(document).ready(function() {
	$('.popup-gallery').magnificPopup({
		delegate: 'a',
		type: 'image',
		tLoading: 'Loading image #%curr%...',
		mainClass: 'mfp-img-mobile',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0,1] // Will preload 0 - before current, and 1 after the current image
		},
		image: {
			tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
			titleSrc: function(item) {
				return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
			}
		}
	});
});



// --------------------------------------------------------------------------------------------------------------------------------

// $(document).ready(function(){
//     $('.counter-value').each(function(){
//         $(this).prop('Counter',0).animate({
//             Counter: $(this).text()
//         },{
//             duration: 3500,
//             easing: 'swing',
//             step: function (now){
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
// });

$(document).ready(function() {
    // call newly created function
    setAnimation();
  });
  
  // add scroll event to check for animation on scroll
  $(document).scroll(function() {
    // call newly created function
    setAnimation();
  });
  
  // Create new function which will trigger your animation
  function setAnimation() {
    // add additional class pending to your .counter-value element to check whether animation is pending or not
    // retrieve only pending elements and loop over it
    $('.counter-value.pending').each(function() {
      // check if element is in view and visible
      var isElementInView = Utils.isElementInView($(this), false);    
      if (isElementInView) {
        // if visible then remove class pending so it won't animate multiple times
        $(this).removeClass('pending');
        // initialize animation
        $(this).prop('Counter', 0).animate({
          Counter: $(this).text()
        }, {
          duration: 3500,
          easing: 'swing',
          step: function(now) {
            $(this).text(Math.ceil(now));
          }
        });
      }
    });
  }
  
  // Added util code from https://stackoverflow.com/questions/487073/how-to-check-if-element-is-visible-after-scrolling
  function Utils() {
  
  }
  
  Utils.prototype = {
    constructor: Utils,
    isElementInView: function(element, fullyInView) {
      var pageTop = $(window).scrollTop();
      var pageBottom = pageTop + $(window).height();
      var elementTop = $(element).offset().top;
      var elementBottom = elementTop + $(element).height();
  
      if (fullyInView === true) {
        return ((pageTop < elementTop) && (pageBottom > elementBottom));
      } else {
        return ((elementTop <= pageBottom) && (elementBottom >= pageTop));
      }
    }
  };
  
  var Utils = new Utils();
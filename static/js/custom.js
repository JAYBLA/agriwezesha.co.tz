(function($) {
	jQuery(document).on('ready', function(){
        // Brand Wrap
		$('.brand-wrap').owlCarousel({
			loop:true,
			nav:false,
			autoplay:true,
			autoplayHoverPause: true,
			mouseDrag: true,
			margin: 0,
			center: false,
			dots: false,
			slideTransition: 'linear',
			autoplayTimeout: 4500,
			autoplayHoverPause: true,
			autoplaySpeed: 4500,
			responsive:{
				0:{
					items:2
				},
				576:{
					items:3
				},
				768:{
					items:4
				},
				992:{
					items:5
				},
				1200:{
					items:5
				}
			}
		});
});
})(jQuery);
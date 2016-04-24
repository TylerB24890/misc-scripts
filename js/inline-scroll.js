/**
 * In page navigation (smooth scroll)
 *
 * Add the class 'inline-link' to any anchor element
 */
jQuery('a.inline-link').click(function(e) {
    var location = jQuery(this).attr('href');
	jQuery('html, body').animate({
		scrollTop: jQuery(location).offset().top
	}, 1200);
    return false;
});

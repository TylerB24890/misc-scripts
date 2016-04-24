/**
 * Fade out hero caption on scroll
 *
 * Use this function and pass a valid selector as the parameter to
 * fade the element out on scroll
 */
function fadeElement(el) {
    //Get the scoll position of the page
    scrollPos = jQuery(this).scrollTop();

    //Scroll and fade out the banner text
    jQuery(el).css({
        'margin-top' : -(scrollPos/3)+"px",
        'opacity' : 1-(scrollPos/225)
    });
}

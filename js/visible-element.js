/**
 * Small jQuery plugin to detect if an element is visible on the screen
 *
 * ex:
 * var el = $('#content');
 * if(el.visible(true)) {
 * 		// Element is visible
 * } else {
 * 		// Element is not visible
 * }
 */
jQuery.fn.visible = function(partial) {
    var $t            = $(this),
        $w            = $(window),
        viewTop       = $w.scrollTop(),
        viewBottom    = viewTop + $w.height(),
        _top          = $t.offset().top,
        _bottom       = _top + $t.height(),
        compareTop    = partial === true ? _bottom : _top,
        compareBottom = partial === true ? _top : _bottom;

    return ((compareBottom <= viewBottom) && (compareTop >= viewTop));
}

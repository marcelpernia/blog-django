$(document).ready(function(){
	// variables
	navicon = $('#navicon');
	menu = $('#menu');
	main = $('#main');
	wd = $(window);

	// responsive menu control
	navicon.click(function(){
		menu.slideToggle('fast');
	});

	// Alto minimo del documento
	function calculateHeight() {
		bodyHeight = wd.height();
		main.css({'minHeight':bodyHeight - 218 + 'px'});
	}
	calculateHeight();

	wd.resize(function(){
		calculateHeight();
	});
});
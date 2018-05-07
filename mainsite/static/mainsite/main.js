var navLogo = document.getElementById('nav-logo');
var screenMaxWidth = window.matchMedia("(max-width: 575.98px)");
var headerHeight;

function logoChange(x) {
    if (x.matches) { // If media query matches
        navLogo.src = logoImg1;
    } else {
        navLogo.src = logoImg2;
    }
}

function adjustCarouselMargin(){
	headerHeight = $("header").css("height");
	$("main").css("margin-top", headerHeight);
	$("header").css("top", 0);
}

logoChange(screenMaxWidth); // Call listener function at run time
screenMaxWidth.addListener(logoChange); // Attach listener function on state changes

adjustCarouselMargin()
window.onresize = function(){adjustCarouselMargin();}

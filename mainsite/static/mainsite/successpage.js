var middle = document.getElementById('success-container');
var footerHeight = $("footer").css("height");
var totalHeight = $(document).height();
var wut = (totalHeight - parseInt(footerHeight) - parseInt(headerHeight));

window.onload = function(){
	middle.style.height = (wut + "px");
}

window.setTimeout(function () {
    location.href = '/';
}, 4000); // refresh/redirect after 5 seconds.

var slides = document.getElementsByClassName("mySlides"); // The slides' containers
var dots = document.getElementsByClassName("demo"); // The thumbnails
var currentSlideId = slides[0].id; // First slide is current slide

slides[0].style.display = "flex"; // First slide is displayed
dots[0].className = dots[0].className += (" active"); // First thumbnail is active

function showSlides(n) { // n is the ambassador_img id or an integer
  var i;

  for (i = 0; i < slides.length; i++) { // For each slide
	slides[i].style.display = "none"; // Make hidden
	dots[i].className = dots[i].className.replace(" active", ""); // Hide thumbnails
  }
  if(n == 1 || n == -1){ // If previous or next button was pressed
	  for (i = 0; i < slides.length; i++) { // For each slide
		  if(slides[i].id == currentSlideId){ // if slide is current slide
			  if(i+n >= slides.length){ // if next slide is past last slide
				  slides[0].style.display = "flex"; // set first slide visible
				  dots[0].className = dots[0].className += (" active"); // make first thumbnail active
				  currentSlideId = slides[0].id; // make first slide current
				  break;
			  }
			  else if (i+n < 0) { // if previous slide is less than the first slide
				slides[slides.length - 1].style.display = "flex"; // make last slide visible
  				dots[slides.length - 1].className = dots[slides.length - 1].className += (" active"); // make last thumbnail active
  				currentSlideId = slides[slides.length - 1].id; // set last slide as current
  				break;
			  }
			  else{ // Do normal thing
				  slides[i+n].style.display = "flex";
				  dots[i+n].className = dots[i+n].className += (" active");
				  currentSlideId = slides[i+n].id;
				  break;
			  }
		  }
	  }
  }
  else{ // If receiving an ambassador id
	  for (i = 0; i < slides.length; i++) { // for each slide
		  if(slides[i].id == n){ // Compare clicked id with iterated slide id
			  slides[i].style.display = "flex"; 
			  dots[i].className = dots[i].className += (" active");
			  currentSlideId = n;
		  }
	  }
  }
}

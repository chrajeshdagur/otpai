/* Live Time from Diff Timezone when access at Location */
function startTime() 
{
	// Time Code
	var today = new Date();
	var h = today.getHours();
	var m = today.getMinutes();
	var s = today.getSeconds();
	m = checkzero(m);
	s = checkzero(s);
	document.getElementById('time').innerHTML = h + ":" + m + ":" + s;					
	
	// Date Code					
	var dt = today.getDate();
	dtt=checkzero(dt);
	document.getElementById('dt').innerHTML = dtt ;

	// Day Code
	var week = new Array();
	week[0] = "Sunday";
	week[1] = "Monday";
	week[2] = "Tuesday";
	week[3] = "Wednesday";
	week[4] = "Thrusday";
	week[5] = "Friday";
	week[6] = "Saturday";					
	var day = week[today.getDay()];
	document.getElementById("day").innerHTML = day;
						
	// Month Code
	var month = new Array();
	month[0] = "January";
	month[1] = "February";
	month[2] = "March";
	month[3] = "April";
	month[4] = "May";
	month[5] = "June";
	month[6] = "July";
	month[7] = "August";
	month[8] = "September";
	month[9] = "October";
	month[10] = "November";
	month[11] = "December";								
	var mnth = month[today.getMonth()];
	document.getElementById("mnth").innerHTML = mnth;					
	
	// Don't no why it used
	var t = setTimeout(startTime, 500);
}

function checkzero(i) 
{
	if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
	return i;
}
/* End Here */




/*Tab Menu Functionality*/

function tabmenu(evt, tabname) {
	var i, tabcontent, tablinks, sidetablinks, sidetabcontent;
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	sidetablinks = document.getElementsByClassName("sidetablinks");
	for (i = 0; i < sidetablinks.length; i++) {
		sidetablinks[i].className = sidetablinks[i].className.replace(" active", "");
	}
	sidetabcontent = document.getElementsByClassName("sidetabcontent");
	for (i = 0; i < sidetabcontent.length; i++) {
		sidetabcontent[i].style.display = "none";
	}
	document.getElementById(tabname).style.display = "block";
	document.getElementById(tabname).children[1].style.display = 'block';
	document.getElementById(tabname).children[0].children[0].className += " active";
	evt.currentTarget.className += " active";
}



function sidemenu(evt, sidename) {
    var i, sidetabcontent, sidetablinks;
    sidetabcontent = document.getElementsByClassName("sidetabcontent");
    for (i = 0; i < sidetabcontent.length; i++) {
        sidetabcontent[i].style.display = "none";
    }
    sidetablinks = document.getElementsByClassName("sidetablinks");
    for (i = 0; i < sidetablinks.length; i++) {
        sidetablinks[i].className = sidetablinks[i].className.replace(" active", "");
    }
    document.getElementById(sidename).style.display = "block";
    evt.currentTarget.className += " active";
}

/* End Here */








/* Carousel */
$(document).ready( function() {
    $('#myCarousel').carousel({
    	interval:   4000
	});
	
	var clickEvent = false;
	$('#myCarousel').on('click', '.nav a', function() {
			clickEvent = true;
			$('.nav li').removeClass('active');
			$(this).parent().addClass('active');		
	}).on('slid.bs.carousel', function(e) {
		if(!clickEvent) {
			var count = $('.nav').children().length -1;
			var current = $('.nav li.active');
			current.removeClass('active').next().addClass('active');
			var id = parseInt(current.data('slide-to'));
			if(count == id) {
				$('.nav li').first().addClass('active');	
			}
		}
		clickEvent = false;
	});
});


/* Youtube */
 $(document).ready(function () {
    $(".arrow-right").bind("click", function (event) {
        event.preventDefault();
        $(".vid-list-container").stop().animate({
            scrollLeft: "+=336"
        }, 750);
    });
    $(".arrow-left").bind("click", function (event) {
        event.preventDefault();
        $(".vid-list-container").stop().animate({
            scrollLeft: "-=336"
        }, 750);
    });
});



/* Hide div*/
$(document).mouseup(function (e)
{
var container = $("#login_acc"); // Give you class or ID
if (!container.is(e.target) && container.has(e.target).length === 0)
// … nor a descendant-child of the container
{
container.hide();
}
});








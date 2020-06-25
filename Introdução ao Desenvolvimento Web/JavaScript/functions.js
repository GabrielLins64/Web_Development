function headerText(title) 
{
	document.getElementById("brasil_h1").innerHTML = title;
};

function sideBarButton(name, tag)
{
	var sidebar = document.getElementById("sidebar");
	var p = document.createElement("p");
	var button = document.createElement("button");
	button.innerHTML = name;
	var usingButton = false;
	button.onclick = function scrollFunc() {
		var div = document.getElementById(tag);
		div.scrollIntoView({
			behavior: 'auto',
			block: 'center',
			inline: 'center'
		});
		if(name === "Topo" || usingButton) {
			return;
		}
		usingButton = true;
		var colors = ["#00FF00", "#00DD00", "#00BB00", "#009900", "#008800", "#007700", window.getComputedStyle(div).borderColor];
		var shadows = ["0px 0px 30px", "0px 0px 20px", "0px 0px 10px", "0px 0px 8px", "0px 0px 5px", "0px 0px 5px", window.getComputedStyle(div).boxShadow];
		for(var i=0; i < colors.length-1; i++) {
			shadows[i] = shadows[i]+" "+colors[i];
		}
		function doSetTimeout(color, shadow, time) { // Needed for setTimeout get to use variables
			setTimeout(function() {
				div.style.borderColor = color;
				div.style.boxShadow = shadow;
			}, time);
		};
		setTimeout(function() { // Deactivate "usingButton" after finish using
			usingButton = false;
		}, 150*colors.length);
		for(var i = 0, time=100; i < colors.length; i++, time+=100) {
			doSetTimeout(colors[i], shadows[i], time);
		}
	};
	sidebar.appendChild(p);
	p.appendChild(button);
};
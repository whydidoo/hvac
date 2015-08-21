$('barometricpressure').bind(function () {
	var temperature=[[-40],[-39],[-38],[-37],[-36],[-35],[-34],[-33],[-32],[-31],[-30],[-29],[-28],[-27],[-26],[-25],
	[-24],[-23],[-22],[-21],[-20],[-19],[-18],[-17],[-16],[-15],[-14],[-13],[-12],[-11],[-10],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],
		[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24],
		[25],[26],[27],[28],[29],[30],[31],[32],[33],[34],[35],[36],[37],[38],[39],[40]];
	var barometricpressure=99;
	var relativities=[10,20,30,40,50,60,70,80,90,100];
	var j=0;
	var i=0;

			if (temperature[0]<0){
            	var saturationeressure=Math.exp((18.74 * temperature[0] - 115.72) / 
            (233.77 + 0.997 * temperature[0]));

        	}else{
            	var saturationpressure=Math.exp((16.57 * temperature[0] - 115.72) /
            	(233.77 + 0.997 * temperature[0]));

            } 

			var humiditycontentForId=(622*relativities[1]/100*saturationpressure)/(barometricpressure-relativities[1]/100*saturationpressure);

			console.log(saturationpressure);
		



	var options = {
 		series: {
        	lines: { 
        		show: true,
        		lineWidth: 3
        	},

        	points: {
            	radius: 1,
            	show: true,
            	color: 'black'
        }
    },
        yaxis: { 
        	max: 30,
        	min: -30,
        	ticks: 60
        },
    	xaxis: { 
    		max: 30,
    		min: 0,
    		ticks: 30
    	},
    	grid: {
    		color: 'black',
    		verticalLines: true,   
        	horizontalLines: true,
        	outlineWidth: 10,
        	mouseActiveRadius: 20,
        	tickColor: 'grey',
			clickable: true,
			hoverable: true
        },
        colors:'black'
	};

    $.plot($("#flot-placeholder"), [[[2,2],[5,5]]],options);

});	
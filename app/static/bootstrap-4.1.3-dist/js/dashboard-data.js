/*Dashboard Init*/
 
"use strict"; 

/*****Ready function start*****/
$(document).ready(function(){
	$('#statement').DataTable({
		"bFilter": false,
		"bLengthChange": false,
		"bPaginate": false,
		"bInfo": false,
	});
	if( $('#chart_2').length > 0 ){
		var ctx2 = document.getElementById("chart_2").getContext("2d");
		var data2 = {
			labels: ["January", "February", "March", "April", "May", "June", "July"],
			datasets: [
				{
					label: "My First dataset",
					backgroundColor: "rgba(230,154,42,1)",
					borderColor: "rgba(230,154,42,1)",
					data: [10, 30, 80, 61, 26, 75, 40]
				},
				{
					label: "My Second dataset",
					backgroundColor: "rgba(234,108,65,1)",
					borderColor: "rgba(234,108,65,1)",
					data: [28, 48, 40, 19, 86, 27, 90]
				},
				{
					label: "My Third dataset",
					backgroundColor: "rgba(70,148,8,1)",
					borderColor: "rgba(70,148,8,1)",
					data: [8, 28, 50, 29, 76, 77, 40]
				}
			]
		};
		
		var hBar = new Chart(ctx2, {
			type:"horizontalBar",
			data:data2,
			
			options: {
				tooltips: {
					mode:"label"
				},
				scales: {
					yAxes: [{
						stacked: true,
						gridLines: {
							color: "#878787",
						},
						ticks: {
							fontFamily: "Roboto",
							fontColor:"#878787"
						}
					}],
					xAxes: [{
						stacked: true,
						gridLines: {
							color: "#878787",
						},
						ticks: {
							fontFamily: "Roboto",
							fontColor:"#878787"
						}
					}],
					
				},
				elements:{
					point: {
						hitRadius:40
					}
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				maintainAspectRatio:false,
				legend: {
					display: false,
				},
				
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Roboto'"
				}
				
			}
		});
	}
	if( $('#chart_6').length > 0 ){
		var ctx6 = document.getElementById("chart_6").getContext("2d");
		var data6 = {
			 labels: [
			"organic",
			"Referral",
			"Other"
		],
		datasets: [
			{
				data: [200,50,250],
				backgroundColor: [
					"#177ec1",
					"#469408",
					"#e69a2a",
				],
				hoverBackgroundColor: [
					"#177ec1",
					"#469408",
					"#e69a2a",
				]
			}]
		};
		
		var pieChart  = new Chart(ctx6,{
			type: 'pie',
			data: data6,
			options: {
				animation: {
					duration:	3000
				},
				responsive: true,
				maintainAspectRatio:false,
				legend: {
					display:false
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Roboto'"
				},
				elements: {
					arc: {
						borderWidth: 0
					}
				}
			}
		});
	}
	if($('#morris_extra_line_chart').length > 0) {
		var data=[{
            period: 'Sun',
            Visitors:978
        }, {
            period: 'Mon',
            Visitors:1021
        }, {
            period: 'Tue',
            Visitors:1032
        }, {
            period: 'Wed',
            Visitors:955
        }, {
            period: 'Thu',
            Visitors:991
        }, {
            period: 'Fri',
            Visitors:1191
        },
         {
            period: 'Sat',
            Visitors:1399
        }];
		var dataNew = [{
            period: 'Jan',
            Visitors:15676
        }, 
		{
            period: 'Feb',
            Visitors:15016
        },
		{
            period: 'March',
            Visitors:14234
        },
		{
            period: 'April',
            Visitors:17685
        },
		{
            period: 'May',
            Visitors:17654
        },
		{
            period: 'June',
            Visitors:13200
        },
		{
            period: 'July',
            Visitors:15021
        },
		{
            period: 'Aug',
            Visitors:14532
        },
		{
            period: 'Sep',
            Visitors:15322
        },
		{
            period: 'Oct',
            Visitors:15998
        },
		{
            period: 'Nov',
            Visitors:16001
        },
		{
            period: 'Dec',
            Visitors:15400
        }
		];
		var lineChart = Morris.Line({
        element: 'morris_extra_line_chart',
        data: data ,
        xkey: 'period',
        ykeys: ['Visitors'],
        labels: ['Visitors'],
        pointSize: 2,
        fillOpacity: 0,
		lineWidth:2,
		pointStrokeColors:['#e69a2a'],
		behaveLikeLine: true,
		gridLineColor: '#878787',
		hideHover: 'auto',
		lineColors: ['#e69a2a'],
		resize: true,
		redraw: true,
		gridTextColor:'#878787',
		gridTextFamily:"Roboto",
        parseTime: false
    });

	}
	/* Switchery Init*/
	var elems = Array.prototype.slice.call(document.querySelectorAll('.js-switch'));
	$('#morris_switch').each(function() {
		new Switchery($(this)[0], $(this).data());
	});
	var swichMorris = function() {
		if($("#morris_switch").is(":checked")) {
			lineChart.setData(data);
			lineChart.redraw();
		} else {
			lineChart.setData(dataNew);
			lineChart.redraw();
		}
	}
	swichMorris();	
	$(document).on('change', '#morris_switch', function () {
		swichMorris();
	});
	
});
/*****Ready function end*****/

/*****Load function start*****/
//$(window).load(function(){
//	window.setTimeout(function(){
//		$.toast({
//			heading: 'Welcome to Doodle',
//			text: 'Use the predefined ones, or specify a custom position object.',
//			position: 'top-right',
//			loaderBg:'#e69a2a',
//			icon: 'success',
//			hideAfter: 3500, 
//			stack: 6
//		});
//	}, 3000);
//});
/*****Load function* end*****/

var sparklineLogin = function() { 
	if( $('#sparkline_1').length > 0 ){
		$("#sparkline_1").sparkline([2,4,4,6,8,5,6,4,8,6,6,2 ], {
			type: 'line',
			width: '100%',
			height: '35',
			lineColor: '#177ec1',
			fillColor: 'rgba(23,126,193,.2)',
			maxSpotColor: '#177ec1',
			highlightLineColor: 'rgba(0, 0, 0, 0.2)',
			highlightSpotColor: '#177ec1'
		});
	}	
	if( $('#sparkline_2').length > 0 ){
		$("#sparkline_2").sparkline([0,2,8,6,8], {
			type: 'line',
			width: '100%',
			height: '35',
			lineColor: '#177ec1',
			fillColor: 'rgba(23,126,193,.2)',
			maxSpotColor: '#177ec1',
			highlightLineColor: 'rgba(0, 0, 0, 0.2)',
			highlightSpotColor: '#177ec1'
		});
	}	
	if( $('#sparkline_3').length > 0 ){
		$("#sparkline_3").sparkline([0, 23, 43, 35, 44, 45, 56, 37, 40, 45, 56, 7, 10], {
			type: 'line',
			width: '100%',
			height: '35',
			lineColor: '#177ec1',
			fillColor: 'rgba(23,126,193,.2)',
			maxSpotColor: '#177ec1',
			highlightLineColor: 'rgba(0, 0, 0, 0.2)',
			highlightSpotColor: '#177ec1'
		});
	}
	if( $('#sparkline_4').length > 0 ){
		$("#sparkline_4").sparkline([0,2,8,6,8,5,6,4,8,6,6,2 ], {
			type: 'bar',
			width: '100%',
			height: '50',
			barWidth: '5',
			resize: true,
			barSpacing: '5',
			barColor: '#e69a2a',
			highlightSpotColor: '#e69a2a'
		});
	}	
}
var sparkResize;
	$(window).resize(function(e) {
		clearTimeout(sparkResize);
		sparkResize = setTimeout(sparklineLogin, 200);
	});
sparklineLogin();
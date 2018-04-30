
function getData(){
    $.get('/data.json',function(data){
	//convert the string data into a dictionary
	weather = JSON.parse(data);
	//update the DOM with the new values
	$("#indoor_temp").text(weather.indoor_temp)
	$("#indoor_humidity").text(weather.indoor_humidity)
	$("#outdoor_temp").text(weather.outdoor_temp)
	$("#outdoor_humidity").text(weather.outdoor_humidity)
	//make other adjustments to UI based on these values
	
	//or use a gauge from https://canvas-gauges.com/
	//see: https://canvas-gauges.com/documentation/user-guide/configuration
	
	$("#indoor_temp_gauge").attr("data-value",weather.indoor_temp)
	$("#outdoor_temp_gauge").attr("data-value",weather.outdoor_temp)
	$("#indoor_humidity_gauge").attr("data-value",weather.indoor_humidity)
	$("#outdoor_humidity_gauge").attr("data-value",weather.outdoor_humidity)
    });
}
//runs as soon as document is ready
$(function(){
    setInterval(getData,1000);
})

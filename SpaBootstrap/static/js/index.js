$(document).ready(function(){
    $("#aboutbutton").click(function(){
        $.get("/about", function(data, status){
		$("#city").load("/about");
        });
    });

    $("#gallerybutton").click(function(){
        $.get("/gallery", function(data, status){
		$("#city").load("/gallery");
        });
    });

    $("#contactbutton").click(function(){
        $.get("/contact", function(data, status){
		$("#city").load("/contact");
        });
    });
});
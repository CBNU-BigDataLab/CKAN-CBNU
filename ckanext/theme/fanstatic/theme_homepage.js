$(function(){
	
	$("#tab1").click(function(){
		$("#tab-content").html("");
		$.ajax({
			url: "http://210.115.182.219/api/3/action/organization_list?all_fields=true",
			method: "GET",
			success: function(data) {
				console.log(data);
				for(var i=0; i<data.result.length;i++){
					$("#tab-content").append("<div class='col-md-4'><div class='item'><a href='/organization/" + data.result[i].name + "'>" + data.result[i].display_name + "</a></div></div>");
				}
                                $("#tab-content").append("<div class='col-md-4'><div class='item'><a href='/organization'></a></div></div>");
			}
		});
	});
        $("#tab2").click(function(){
                $("#tab-content").html("");
                var topics = [
			"국제보건의료",
			"의약품",
			"질병",
			"건강",
			"환자",
			"병원",
			"노인",
			"진료행위",
			"의료",
			"통계",
			"임상Data",
			"장애",
			"치료",
			"연구",
			"기타"
		]
                $.each(topics, function(index, value){
                        $("#tab-content").append("<div class='col-md-4'><div class='item'><a href='/dataset?topic="+ value +"'>" + value + "</a></div></div>");
                });
        });

	$("#tab1").trigger("click");
        $("#datasets,#sub-menu").mouseover(function(){
		$("#sub-menu,#sub-menu-caret").show();
	});

	$("#sub-menu").mouseleave(function(){
		$("#sub-menu,#sub-menu-caret").hide();
	});
});

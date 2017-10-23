$(function(){
	
	$("#tab1").click(function(){
		$("#tab-content").html("");
                var contents = [
			"질병관리본부",
			"국립정신건강센터",
			"국립나주병원",
			"국립춘천병원",
			"국립공주병원",
			"국립공주병원",
			"국립마산병원",
			"국립목포병원",
			"오송생명과학단지지원센터",
			"국립부족병원",	
			"국립재활원",
			"국립망향의동산관리원"
		];
		for(var i=0;i<12;i++){
			$("#tab-content").append("<div class='col-md-4'><div class='item'><a href='javascript:;'>"+ contents[i] +"</a></div></div>");
		}
	});
        $("#tab2").click(function(){
                $("#tab-content").html("");
                for(var i=0;i<12;i++){
                        $("#tab-content").append("<div class='col-md-4'><div class='item'>국립정신건강센터</div></div>");
                }
        });
        $("#tab3").click(function(){
                $("#tab-content").html("");
                for(var i=0;i<12;i++){
                        $("#tab-content").append("<div class='col-md-4'><div class='item'>질병관리본부</div></div>");
                }
        });
        $("#tab4").click(function(){
		$("#tab-content").html("");
                for(var i=0;i<12;i++){
                        $("#tab-content").append("<div class='col-md-4'><div class='item'>질병관리본부</div></div>");
                }                
        });

	$("#tab1").trigger("click");
        $("#datasets").click(function(){
		//$("#sub-menu-caret").toggle();
		$("#sub-menu,#sub-menu-caret").toggle();
	});
});

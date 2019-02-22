function update(){
	$(".node").each(function(){
		submenu = $(this).next(".container");
		// alert(submenu);
		if(submenu.size() != 0){
			if(submenu.is(":hidden")){
				$(this).css("background-color","yellow");
			}else{
				$(this).css("background-color","white");
			}
		}else{
			$(this).css("background-color","white");
		}
	});
}

$(function(){

	$(".node").each(function(){
		divs = $(this).nextAll();
		this_level = parseInt($(this).attr("level"));
		children = $();
		divs.each(function(){
			level = parseInt($(this).attr("level"));
			if (level > this_level){
				children = children.add($(this));
				// alert(level)
				// alert("length:" + children.size())
			}else{
				return false;
			}
		});
		// alert("children:"+children.size());
		children.wrapAll("<div class='container'></div>");
	});

	$(".container").hide();
	update();


	$(".node").click(function(){
		submenu = $(this).next(".container");
		submenu.slideToggle("fast");
		submenu.promise().done(function(){
			update();
		});
	});
});

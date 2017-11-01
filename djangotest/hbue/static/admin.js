$(function(){
	//登录模态框
	$('button.smodal').click(function(){
		$('#signin').modal('show');
	});
	
	//评论模态框
	$('button.vmodal').click(function(){

		$('#submit-views').modal('show');
	});
	
	//追加评论
	$('#view-div button').click(function(){		
		$('#message-text').append($(this).text() + " ");
	});
	
	//推荐
	like_i = 0;
	$('button#like').click(function(){
		if(like_i % 2 == 0){
			val = parseInt($('span.count1').html()) + 1;
			$('span.count1').html(val);
			$(this).css({'background':'#1caaea','color':'white'});
		}else{
			val = parseInt($('span.count1').html()) - 1;
			$('span.count1').html(val);
			$(this).css({'background':'white','color':'#1caaea'});
		}
		like_i++;
	});
	
	//不推荐
	unlike_i = 0;
	$('button#unlike').click(function(){
		if(unlike_i % 2 == 0){
			val = parseInt($('span.count2').html()) + 1;
			$('span.count2').html(val);
			$(this).css({'background':'#1caaea','color':'white'});
		}else{
			val = parseInt($('span.count2').html()) - 1;
			$('span.count2').html(val);
			$(this).css({'background':'white','color':'#1caaea'});
		}
		unlike_i++;
	});
	
	cnt = 0;
	$('#star-rate span').click(function(){	
		if(cnt < 5){
			$(this).addClass('glyphicon-star').removeClass('glyphicon-star-empty');
			cnt++;
			score = cnt*2;			
		}
		else{
			score = 10;
		}
		$('span.rate').html(score + '.0');
		
	});

	
});

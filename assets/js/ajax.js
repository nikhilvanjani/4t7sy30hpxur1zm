$(function(){

	$('#search').keyup(function()	{

		$.ajax({
			type: "POST",
			url: "/forum/home/queries/search/",
			data: {
				'search_text' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		});

	});

});

function searchSuccess(data, textStatus, jqXHR)
{
	$('$search-results').html(data);
}


function pasteHTML(event) {
	var pos = document.getElementById("id_body").selectionStart;
	var text = $("#id_body").val();
	var add = event.target.outerHTML;
	$("#id_body").val(text.substring(0, pos) + add + text.substring(pos));
}

$(window).load(function() {
	var images = $(".image-preview");
		$(images).each(function() {
			$(this).on("click", pasteHTML);
		});
});

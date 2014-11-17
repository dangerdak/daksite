function pasteHTML(event) {
	var add;
	var pos = document.getElementById("id_body").selectionStart;
	var text = $("#id_body").val();
	if ( $(event.target).is("figure") ) {
		add = event.target.outerHTML;
	}
	else {
			add = this.outerHTML;
	}
	$("#id_body").val(text.substring(0, pos) + add + text.substring(pos));
}

$(window).load(function() {
	var images = $(".image-preview");
		$(images).each(function() {
			$(this).on("click", pasteHTML);
		});
});

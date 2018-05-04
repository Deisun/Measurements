var textboxIndex = 0;


addTextBox();


function getLength(index) {
    var listItemName = "listItem" + index;

    var element = document.getElementById(listItemName);
    var input = element.getElementsByTagName("input")[0];
    var span = element.getElementsByTagName("span")[0];

    span.innerHTML = input.value.length;

}


function addTextBox() {

    var element = document.getElementById("textBoxList");
    var li = document.createElement("li");
    var input = document.createElement("input");
    var span = document.createElement("span");

    var listItemName = "listItem" + textboxIndex;


    li.setAttribute("id", listItemName);
    span.innerHTML = "0";

    input.type = "text";
    input.setAttribute("onkeyup", "getLength(" + textboxIndex + ")");
    

    li.appendChild(input);
    li.appendChild(span);
    element.appendChild(li);

    textboxIndex++;
}

function removeTextBox() {

	if (textboxIndex > 1) {

	    var element = document.getElementById("textBoxList");
	    element.removeChild(element.lastChild);
	    textboxIndex--;
	}
}
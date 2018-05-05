var textBox = document.getElementById("textBox");

var btnA = document.getElementById("btnA");
var btnB = document.getElementById("btnB");
var btnC = document.getElementById("btnC");
var btnD = document.getElementById("btnD");
var btnE = document.getElementById("btnE");

var backgroundA = document.getElementById("backgroundA");
var backgroundB = document.getElementById("backgroundB");
var backgroundC = document.getElementById("backgroundC");
var backgroundD = document.getElementById("backgroundD");
var backgroundE = document.getElementById("backgroundE");


btnA.onclick = function () { textBox.style.color = "#8BE8CB"; };
btnB.onclick = function() { textBox.style.color = "#303633"; };
btnC.onclick = function() { textBox.style.color = "#8DB580"; };
btnD.onclick = function() { textBox.style.color = "#9C7A97"; };
btnE.onclick = function() { textBox.style.color = "#AC7B7D"; };

backgroundA.onclick = function () { textBox.style.backgroundColor = "#8BE8CB"; };
backgroundB.onclick = function() { textBox.style.backgroundColor = "#303633"; };
backgroundC.onclick = function() { textBox.style.backgroundColor = "#8DB580"; };
backgroundD.onclick = function() { textBox.style.backgroundColor = "#9C7A97"; };
backgroundE.onclick = function() { textBox.style.backgroundColor = "#AC7B7D"; };





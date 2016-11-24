$(document).ready(function(){
  var left = 300
  $("p:nth-of-type(2)").append("<p style = 'color:red' id = 'counter'>Characters left: </p>")
  left = 300 - $("#id_text").val().length;
  $("#counter").append(left);

$('#id_text').bind('input propertychange', (function () {
    left = 300 - $(this).val().length;
    $('#counter').text(' Characters left: ' + left);
}));
})

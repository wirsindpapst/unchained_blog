$(document).ready(function(){
  var left = 500;
  $("p:nth-of-type(2)").append("<p style = 'color:green' id = 'counter'>Characters left: </p>");
  left = 500 - $("#id_bio").val().length;
  $("#counter").append(left);

  $('#id_bio').bind('input propertychange', (function () {
    left = 500 - $(this).val().length;
    $('#counter').text(' Characters left: ' + left);
  }));
});

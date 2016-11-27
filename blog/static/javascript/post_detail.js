$(document).ready(function() {
  $("#add-comment").click(function(){
    $(".comment-form").show();
    $(this).hide();
  });
  $("#add-category").click(function(){
    $(".category-form").show();
    $(this).hide();
  });
  $(".like-btn btn btn-default").click(function(){
    $(this).hide();
  });
});

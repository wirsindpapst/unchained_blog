$(document).ready(function(){
  $('.like-btn').click(function(event){
    event.preventDefault();
    $.ajax({
         type: "POST",
         url: "{% url 'like' %}",
         data: {'pk': $(this).attr('name'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
         dataType: "json",
         success: function(response) {
                alert('Company likes count is now ');
          },
         error: function(rs, e) {
                alert('Something went wrong.');
         }
    });
  });
});

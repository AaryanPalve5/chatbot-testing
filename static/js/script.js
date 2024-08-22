$(document).ready(function(){
    $("#jokeForm").on("submit", function(event){
        event.preventDefault();

        var user_input = $("#user_input").val();

        $.ajax({
            url: "/",
            type: "POST",
            data: { user_input: user_input },
            success: function(response){
                $("#response").text(response.response);
            },
            error: function(){
                $("#response").text("An error occurred, please try again.");
            }
        });
    });
});

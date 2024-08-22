$(document).ready(function(){
    $("#jokeForm").on("submit", function(event){
        event.preventDefault();

        var user_input = $("#user_input").val().trim();

        if (!user_input) {
            $("#response").text("Please enter a valid input.");
            return;
        }

        $("#response").text("Loading...");

        $.ajax({
            url: "/",
            type: "POST",
            data: { user_input: user_input },
            contentType: "application/x-www-form-urlencoded",
            success: function(response){
                $("#response").text(response.response);
            },
            error: function(xhr, status, error){
                $("#response").text("Error: " + xhr.responseText);
            }
        });
    });
});

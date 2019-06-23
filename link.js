
function getList(user) {
    var url;
    url = "http://localhost:5000/?u=" + user;
    return url;
}

$(document).ready(function () {

    $("#mainform").submit(function (event) {
        event.preventDefault();
        var user = $("#username").val();

        var url = getList(user);
        $.get(url, function (data) {
            $("#output").html(function () {
                return data;
            });
        });
    });

});
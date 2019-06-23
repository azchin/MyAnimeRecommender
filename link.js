

function formatData(input) {
    var pairs = input.split("~");
    var pLen = pairs.length - 1;
    var str = "";
    for(i = 0; i < pLen; ++i) {
        var temp = pairs[i].split("`");
        str = str + "<a href=\"" + temp[1] + "\">" + temp[0] + "</a><br>";
    }
    return str;
}

function getList(user) {
    var url;
    url = "https://my-anime-recommender.herokuapp.com/?u=" + user;
    //url = "http://localhost:5000/?u=" + user;
    //url = "http://localhost:5000/test/";
    return url;
}

$(document).ready(function () {

    $("#mainform").submit(function (event) {
        event.preventDefault();
        var user = $("#username").val();
        /*$("#clicked").html(function() {
            return "You clicked the button!";
        });*/
        var url = getList(user);
        $.get(url, function (data) {
            $("#output").html(function () {
                //return data;
                return formatData(data);
            });
        });
    });

});
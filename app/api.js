var username = "";
var password = "";
var rootUrl = "http://127.0.0.1/storynode/api/";

$.ajaxSetup({
    type: "POST",
    username: username,
    password: password,
    dataType: "json"
});

$.ajax({
    url: rootUrl + "comment",
    data: {}
}).done(function(returnedData){
    console.log(JSON.stringify(returnedData));
});

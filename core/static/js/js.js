var redirect_uri = "http://127.0.0.1:8000/";
var client_id = "790564c68ae942889364b0529aa31d7c";
const AUTHORIZE = "https://accounts.spotify.com/authorize";

function requestAuthorization(){

    var redirect_uri = "http://127.0.0.1:8000/";
    var client_id = "790564c68ae942889364b0529aa31d7c";
    const AUTHORIZE = "https://accounts.spotify.com/authorize";

    let url = AUTHORIZE;
    url += "?client_id=" + client_id;
    url += "&response_type=code";
    url += "&redirect_uri=" + encodeURI(redirect_uri);
    url += "&show_dialog=true";
    url += "&scope=playlist-modify-public playlist-modify-private";
    window.location.href = url;
}

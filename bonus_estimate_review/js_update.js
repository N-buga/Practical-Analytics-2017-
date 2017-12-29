function sendQuery() {
    var input = document.getElementById("review");
    var query = input.value;
    var connection = new WebSocket('ws://localhost:9999');
    connection.onopen = function () {
        connection.send(query);
    };

    connection.onmessage = function (msg) {
        var elem = document.getElementById("mark");
        elem.textContent = msg.data;
        if (msg.data == "0.0") {
            elem.setAttribute("style","color: red; font-size:24px")
        } else {
            elem.setAttribute("style","color: green; font-size:24px")
        }
    };
}
var express = require("express");
var http = require("http");
var app = express();
var bodyParser = require("body-parser");
var server = http.createServer(app);
server.listen(80, () => {
  console.log("시작");
});
app.use(express.static(__dirname + "/web"));
app.use(bodyParser.json());
app.get("/", function (req, res) {
  console.log("[Server] GET : /");
  res.send("Hi, Client, I am a server");
});
app.post("/", (req, res) => {
  console.log("[Server] POST : " + JSON.stringify(req.body));
  res.send(`post value is : ` + req.body.Client + ``);
});

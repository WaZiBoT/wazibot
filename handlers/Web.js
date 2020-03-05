const client = require("../index.js");
const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);

app.get("/", (req, res) => {
  console.log(new Date() + " - Ping Received!");
  return res.status(200).send(";)");
});

setInterval(() => {
  http.get(`http://${process.env.PROJECT_DOMAIN}.glitch.me`)
}, 280000);

server.listen(process.env.PORT, () => {
  console.log("Listening on port *"+process.env.PORT)
});
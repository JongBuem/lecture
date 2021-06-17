var net = require('net');
function getConnection(connName){
  var client = net.connect({port: 8107, host:'172.19.250.181'}, function() {
    console.log(connName)
    console.log("클라이언트 접속")
    this.setTimeout(500);
    this.setEncoding('utf8');
    this.on('data', function(data) {
        console.log(data)
      this.end();
    });
    this.on('end',()=>{
    });
    this.on('error',(err)=>{
        console.log(err)
    });
    this.on('timeout', ()=>{
    });
    this.on('close',()=>{
    });
  });
  return client;
}

function writeData(socket, data){
  var success = !socket.write(data);
  if (!success){
    (function(socket, data){
      socket.once('drain', function(){
        writeData(socket, data);
      });
    })(socket, data);
  }
}
var Alice = getConnection("Alice's Connection");
var Bob = getConnection("Bob's Connection");
writeData(Alice, "Alice|Hi, Server");
writeData(Bob, "Bob|Hello, Server");

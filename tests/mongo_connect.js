var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://<user>:<pass>@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("Innoventory");
  var query = { item: "Clam Nectar" };
  dbo.collection("Grocery").find(query).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});
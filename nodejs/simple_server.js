const app = require("express")();

app.get("/", (req,res) => res.send("created by FT") )

app.listen(9999, ()=>console.log("listening on 9999..."))


var express = require('express');
var app = express();

app.use(express.static(__dirname + '/public'));

app.get('/', function(req, res) {

	app.engine('html', require('ejs').renderFile);
	app.set('view engine', 'html');

	res.render('Cover', {
		title : 'Tutorial'
	});

});

app.get('/logs', function(req, res) {
        
    app.engine('html', require('ejs').renderFile);
    app.set('view engine', 'html');
    
    res.render('logs', {
        title : 'Logs'
    });
        
});

app.get('/tutorial', function(req, res) {
        
    app.engine('html', require('ejs').renderFile);
    app.set('view engine', 'html');
    
    res.render('tutorial', {
        title : 'Tutorial'
    });
        
});

var server = app.listen(80, function() {

	var host = server.address().address
	var port = server.address().port

	console.log("Example app listening at http://%s:%s", host, port)

})

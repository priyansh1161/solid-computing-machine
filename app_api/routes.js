var express = require('express');
var router = express.Router();
var nearbyLocations = require('./controllers/nearbyLocations');
var user = require('./controllers/user');
router.get('/', user.validateKey,nearbyLocations);
router.get('/signup',user.addUser);
router.get('/login',user.loginUser);
module.exports = router;
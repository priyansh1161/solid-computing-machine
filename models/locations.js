var mongoose = require('mongoose');

var locationSchema = new mongoose.Schema({
    type : String,
    obj : Object,
    // Always store coordinates longitude, latitude order.
    coord: {
        type: [Number],
        index: '2dsphere'
    },
});

mongoose.model('Location', locationSchema);
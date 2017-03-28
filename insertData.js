var mongoose = require('mongoose');
var Location = mongoose.model('Location');
var fs = require('fs');

fs.readFile('./dataset.json','utf-8',(err, data) => {
    if(err)
        console.log(err);
    else {
        let dataSet = JSON.parse(data);
        for (let curr of dataSet){
            let lat = parseFloat(curr.LATITUDE_x) || parseFloat(curr.LATITUDE_y);
            let long = parseFloat(curr.LONGITUDE_x) || parseFloat(curr.LONGITUDE_y);
            console.log(lat,long);
            Location.create({
                obj : curr,
                coord : [long,lat]
            })
                .then((data) => console.log('inserted'))
                .catch( err => console.log(err));
        }
    }
});

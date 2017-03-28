var mongoose = require('mongoose');
const exec = require('child_process').exec;
const fs = require('fs');
var Location = mongoose.model('Location');
function jsonResponse(res,status,json){
    status = status || 200;
    res.status(status);
    res.json(json);
}
function predictIntensity(data,req,res) {
    let forpy = [];
    for(let curr of data){
        forpy.push(curr.obj.obj);
    }
    fs.writeFile('./forpy.json',JSON.stringify(forpy) , (err) => {
        if (err) {
            jsonResponse(res, 200, {data});
            console.error(`fs error: ${err}`);
        }
        else {
            exec('', (error, stdout, stderr) => {
                if (error) {
                    console.error(`exec error: ${error}`);
                    jsonResponse(res, 200, {data});
                }
                else {
                    console.log(stdout);
                    console.log(typeof stdout);
                    jsonResponse(res, 200, {data, stdout});
                }
            });
        }
    });
}
module.exports = (req, res) => {
    var lng = parseFloat(req.query.lng);
    var lat = parseFloat(req.query.lat);
    var maxDistance = parseFloat(req.query.maxDistance);
    if(!lng || !lat || !maxDistance){
        jsonResponse(res,404,{status:'Bad request'});
        return;
    }
    var point = {
        type : 'Point',
        coordinates: [lng,lat]
    };
    var geoOptions = {
        spherical : true,
        num : 10,
        maxDistance : maxDistance*1000
    };
    Location.geoNear(point,geoOptions,function (err,results,status) {
        if(err){
            jsonResponse(res,500,err);
        }
         predictIntensity(results,req,res);

    });
};
const mongoose = require('mongoose');
const User = mongoose.model('User');

function addUser (req,res){
    if(req.query){
        var user = new User();
        user.f_name = req.query.f_name;
        user.l_name = req.query.l_name;
        user.email = req.query.email;
        user.phone = req.query.phone;
        user.setPassword(req.query.password,function () {
            user.save(function (err,savedUser) {
                if(err){
                    console.log(err);
                    next(err);
                }
                else{
                    req.session.accessToken = savedUser._id;
                    res.json({key : savedUser._id});
                }
            });
        });

    }
}
function loginUser (req, res){
    if(req.query.phone && req.query.password){
        User
            .findOne({phone : req.query.phone})
            .select('name password salt')
            .exec(function (err,user) {
                console.log(user,'user');
                if(err){
                    res.json(err);
                }
                if(!user){
                    res.json(new Error('Invalid userName'));
                }
                else{
                    console.log('dxfgch');
                    var isValidated = user.validatePassword(req.query.password);
                    console.log('cf',isValidated);
                    if(!isValidated){
                        req.json(new Error('Invalid Password'));
                    }
                    else{
                        console.log('this');
                        req.session.accessToken = user._id;
                        res.json({key : user._id });
                    }
                }
            });
    }
    else
        res.send(new Error('invalid args'));
}
function validateKey(req,res,next){
    if(!req.query.key){
        res.send(new Error('login again'))
    }
    console.log('key');
    User
        .findById(req.query.key)
        .then((user) => {
            console.log(user);
            if(user._id){
                console.log('asdas');
                next();
            }
            else
                res.send(new Error('login again'))

        })
        .catch((err) => res.send(err));
}
module.exports = {
    addUser,
    loginUser,
    validateKey
};
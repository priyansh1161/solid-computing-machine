var mongoose = require('mongoose');
var crypto = require('crypto');
var Schema = mongoose.Schema;

var UserSchema = new Schema({
    f_name : {type : String , required : true },
    l_name : {type : String , required : true },
    email : {type : String , required : true , unique : true},
    phone : {type : String, required : true, unique : true},
    salt : String,
    password  : String
});

UserSchema.methods.setPassword = function (password,cb) {
    console.log(password,this,this.name);
    var salt = crypto.randomBytes(32).toString('hex');
    crypto.pbkdf2(password,salt,1000,64,'sha256',function (err,key) {
        if(err) throw err;
        else {

            this.salt = salt;
            this.password = key.toString('hex');
            cb.apply(this);
        }
    }.bind(this));
};
UserSchema.methods.validatePassword = function (password) {

    return crypto.pbkdf2Sync(password,this.salt,1000,64,'sha256').toString('hex') == this.password;
};
mongoose.model('User',UserSchema);
module.exports = UserSchema;
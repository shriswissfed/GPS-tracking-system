var nodemailer = require("nodemailer");
var express = require('express');
var router = express.Router();
var transporter;
//app.use('/sayHello', router);
router.post('/', main);

function main(req, res) {
        transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'prem21071994@gmail.com',
            pass: '9952175441'
        }
    });
}
var mailOptions = {
    from: 'prem21071994@gmail.com',
    to: 'xxpunithxx@gmail.com',
    subject: 'Email Example',
    text: 'Hellooooooooo'
};
transporter.sendMail(mailOptions, function(error, info){
    if(error){
        console.log(error);
        res.json({Not sent: 'error'});
    }else{
        console.log('Message sent: ' + info.response);
        res.json({sent: info.response});
    };
};
/*transporter.sendMail({
from: 'prem21071994@gmail.com',
  to: 'xxpunithxx@gmail.com',
  subject: 'hello world!',
  text: 'hello world!'
});*/
module.exports = router;

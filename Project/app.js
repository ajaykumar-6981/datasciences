const express=require('express');
const bodyParser=require('body-parser');

const feedRoutes=require('./routes')
const app=express();

app.use(bodyParser.json());   //application/json
app.use('/feed',feedRoutes);

app.use((req,res,next)=>{
    res.status(200).json({
        message:'Its works!'
    });
});

app.listen(3000);

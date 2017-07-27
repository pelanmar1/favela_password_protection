/*
Originally found at https://cssdeck.com/labs/login-form-using-html5-and-css3

by: https://cssdeck.com/user/kamalchaneman

*/
var times=[];
var numBackspaces=0;
var currentStatus=0;

document.getElementById("add").addEventListener("click", function(){
    var feat=getFeatures();
    var data = {
        features:feat
    };
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:5000/login',
        data: data
});
    
});

document.getElementById("train").addEventListener("click", function(){
    
});

document.getElementById("test").addEventListener("click", function(){
    changeAlert(1);
    event.preventDefault();
});


var input = document.getElementById('password');
input.onkeydown = function() {
    var key = event.keyCode || event.charCode;
    if (key != 8 && input.value.length==0){
        times = [];
        numBackspaces=0;
        start();
    }else if(key != 8 && input.value.length>0){
        times.push(end())
        start();
    }else if(key == 8){
            numBackspaces++;
            times.pop();
    }
};


var getFeatures = function(){
    features = [];
    if(times.length>0){
        averageTime = 0;
        maxTime = times[0];
        totalTime = 0;
        // Get average time
        for(var i = 0;i<times.length;i++){
            totalTime+=times[i];
            if(times[i]>maxTime)
                maxTime = times[i];
        }
        averageTime = totalTime/times.length;
        // Get max time between strokes
        features = [totalTime,averageTime,maxTime,numBackspaces];
    }
    return features;
}

var startTime, endTime;

function start() {
  startTime = new Date();
};

function end() {
  endTime = new Date();
  var timeDiff = endTime - startTime; //in ms
  // strip the ms
  timeDiff /= 1000;
  return timeDiff;
}




var changeAlert = function(status){
    currentStatus = status;
    var classes =['alert alert-warning','alert alert-success','alert alert-danger'];
    document.getElementById('status').className = classes[currentStatus];
    var messages = [' ',' - Welcome',' - Access Denied'];
    var title = 'FAVELA Password Protection';
    document.getElementById('title').innerText=title+messages[status];
}
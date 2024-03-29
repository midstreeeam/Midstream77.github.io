function getStyle(obj,name){
    if(window.getComputedStyle){
        return getComputedStyle(obj,null)[name];
    }
    else{
        //for ie8
        return obj.currentStyle[name];
    }
}

/*
*obj: the obj need move
*speed: Int (absolute position)
*target: Int (absolute position)
*attr: String, "left", "top", "width"
*callback: function, not necessary
*/
function move(obj,attr,target,speed,callback){
    clearInterval(obj.timer);
    var current = parseInt(getStyle(obj,attr));
    if(current>target){
        speed = -speed;
    }
    obj.timer = setInterval(function(){
        var oldValue = parseInt(getStyle(obj,attr));
        var newValue = oldValue + speed;
        if((speed<0&&newValue<target)||(speed>0&&newValue>target)){
            newValue=target;
        }
        obj.style[attr] = newValue + "px";
        if(newValue == target){
            clearInterval(obj.timer);
            callback&&callback();
        }
    },30);
}

function move_second(obj,attr,target,speed,callback){
    clearInterval(obj.timer2);
    var current = parseInt(getStyle(obj,attr));
    if(current>target){
        speed = -speed;
    }
    obj.timer2 = setInterval(function(){
        var oldValue = parseInt(getStyle(obj,attr));
        var newValue = oldValue + speed;
        if((speed<0&&newValue<target)||(speed>0&&newValue>target)){
            newValue=target;
        }
        obj.style[attr] = newValue + "px";
        if(newValue == target){
            clearInterval(obj.timer2);
            callback&&callback();
        }
    },30);
}
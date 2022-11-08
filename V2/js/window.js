//list_icon click
var list_icon = document.getElementsByClassName("list_icon")[0];
var clicked = false;

function list_icon_click(){

    if(clicked){
        var nav_panel_element_show = new Array();
        var icon_dis_hidden = new Array();
    
        var cover_panel_show = document.getElementsByClassName("cover_panel_show")[0];
        nav_panel_element_show = document.getElementsByClassName("nav_panel_element_show");
        icon_dis_hidden = document.getElementsByClassName("icon_dis_hidden");

        cover_panel_show.className = "cover_panel_hidden";

        var len1 = nav_panel_element_show.length;
        var len2 = icon_dis_hidden.length;
        for(var i = 0;i<len1-1;i++){
            nav_panel_element_show[0].className = "nav_panel_element";
        }
        nav_panel_element_show[0].className = "nav_panel_element_hidden";

        for(var i = 0;i<len2;i++){
            icon_dis_hidden[0].className = "icon_dis";
        }
        clicked = false;
    }else{
        var nav_panel_element = new Array();
        var icon_dis = new Array();
    
        var nav_panel_element_hidden = document.getElementsByClassName("nav_panel_element_hidden")[0];
        var cover_panel_hidden = document.getElementsByClassName("cover_panel_hidden")[0];
        nav_panel_element = document.getElementsByClassName("nav_panel_element");
        icon_dis = document.getElementsByClassName("icon_dis");

        cover_panel_hidden.className = "cover_panel_show";

        var len1 = nav_panel_element.length;
        var len2 = icon_dis.length;
        for(var i = 0;i<len1;i++){
            nav_panel_element[0].className = "nav_panel_element_show";
        }
        nav_panel_element_hidden.className = "nav_panel_element_show";
        for(var i = 0;i<len2;i++){
            icon_dis[0].className = "icon_dis_hidden";
        }
        clicked = true;
    }
}


//mobile--pc change
function resize() {
    function to_mobile() {
        if (document.getElementsByClassName("cover_left")[0]) {
            document.getElementsByClassName("cover_left")[0].className = "cover_top";
            document.getElementsByClassName("content_right")[0].className = "content_down";
            //document.getElementsByClassName("cover_last_left")[0].className = "cover_last_top"
            document.getElementsByClassName("cover_panel")[0].className = "cover_panel_hidden";
            var nav_panel_list_icon_hidden = document.getElementsByClassName("nav_panel_list_icon_hidden")[0];
            nav_panel_list_icon_hidden.className = "nav_panel_list_icon";
        }

    }
    function to_pc() {
        if(!document.getElementsByClassName("cover_panel_hidden")[0]){
            try{
                list_icon_click();
            }catch(error){}
        }
        if (document.getElementsByClassName("cover_top")[0]) {
            document.getElementsByClassName("cover_top")[0].className = "cover_left";
            document.getElementsByClassName("content_down")[0].className = "content_right";
            document.getElementsByClassName("cover_panel_hidden")[0].className = "cover_panel";
            nav_panel_list_icon = document.getElementsByClassName("nav_panel_list_icon")[0].className = "nav_panel_list_icon_hidden";
        }
    }
    var w = document.body.clientWidth;
    if (w < 960) {
        to_mobile();
    } else {
        to_pc();
    }
}

window.onresize = function(){
    resize();
};


//moving part
window.onload = function() {
    var btn = document.getElementById("btn_start");
    var cover = document.getElementsByClassName("cover")[0];
    var nav_panel_hidden = document.getElementsByClassName("nav_panel_hidden")[0];
    var clickable = true;

    //judge if the initial is mobile or pc
    //pc at first
    var w = document.body.clientWidth;

    if (document.getElementsByClassName("cover")[0]) {
        if (w >= 960) {
            btn.onclick = function () {
                if (clickable) {
                    move(cover, "width", document.body.clientWidth * 0.3, 70, function () {
                        cover.className = "cover_left";
                    });
                    move(nav_panel_hidden, "height", document.body.offsetHeight * 0.16, 8, function () {
                        nav_panel_hidden.removeAttribute("style");
                        nav_panel_hidden.className = "nav_panel";
                    })
                    btn.innerText = "home";
                    btn.id = "btn_home";
                    clickable = false;
                }

            }
        } else {//mobile
            var content_right = document.getElementsByClassName("content_right")[0];
            var nav_panel_list_icon_hidden = document.getElementsByClassName("nav_panel_list_icon_hidden")[0];

            var height = document.body.clientHeight;
            btn.onclick = function () {
                if (clickable) {
                    content_right.className = "content_down";
                    move(cover, "height", height * 0.25, 70, function () {
                        cover.className = "cover_top";
                    });
                    move_second(cover, "paddingTop", height * 0.03, 10);
                    document.getElementsByClassName("cover_panel")[0].className = "cover_panel_hidden";
                    nav_panel_hidden.className = "nav_panel";
                    nav_panel_list_icon_hidden.className = "nav_panel_list_icon";
                    btn.innerText = "home";
                    btn.id = "btn_home";
                    clickable = false;
                }
            }
        }
    }

}
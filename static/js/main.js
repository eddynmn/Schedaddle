//Information Type
let contentType = "HELLO"

function sendSchedule (data) {
    fetch('/schedule', {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
                if (data.status == "Success"){
                    hideModal(document.getElementById("myModal"));
                }
            } 
        )
}

function sendInfo() {
    info = {"name":0, "length":0, "deadline":0, "type":0}
    info.name = document.getElementById("name").value;
    info.length = document.getElementById("length").value;
    info.deadline = document.getElementById("deadline").value;
    info.type = "flex";
    console.log(info);
    sendSchedule(info);
}

var fixedType = ""
function sendInfo1() {
    info = {"name1":0, "start":0, "end":0, "type":0}
    info.name1 = document.getElementById("name1").value;
    info.start = document.getElementById("start").value;
    info.end = document.getElementById("end").value;
    info.type = "fixed";
    console.log(info);
    console.log(contentType)
    sendSchedule(info);
}

function buttonPressed(id){
    document.getElementById(id).setAttribute("class", "buttonPresssed");
}

function toggleText() {
    
    var text = document.getElementById("appear")
    document.getElementById("appear1").style.display = "none";
    if (text.style.display === "none") {
        text.style.display = "contents";
        contentType = "flex";
    } else {
        text.style.display = "none";
        contentType = "";
    }
}

function toggleText1() {
    var text = document.getElementById("appear1")
    document.getElementById("appear").style.display = "none";
    if (text.style.display === "none") {
        text.style.display = "contents";
        contentType = "fixed";
    } else {
        text.style.display = "none";
        contentType = "";
    }
}

// var btn = document.getElementById("myBtn");
//     btn.onclick = toggleModal();
function showModal() {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    modal.style.display = "block";
    span.onclick = function() {
        hideModal(modal);
        window.onclick = function(event) {
        if (event.target == modal) {
            hideModal(modal);
        }
        }
    }
}

function hideModal(modal) {
    modal.style.display = "none";
}
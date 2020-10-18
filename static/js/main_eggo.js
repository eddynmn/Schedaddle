sendSchedule = (data) => {
    fetch('schedule', {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => alert(data.data))
}
var variableType = ""
function sendInfo() {
    info = {"name":0, "length":0, "deadline":0, "type":0}
    info.name = document.getElementById("name").value;
    info.length = document.getElementById("length").value;
    info.deadline = document.getElementById("deadline").value;
    // info.type = document.getElementById("type").value;
    console.log(info)
}

var fixedType = ""
function sendInfo1() {
    info = {"name1":0, "start":0, "end":0, "type":0}
    info.name1 = document.getElementById("name1").value;
    info.start = document.getElementById("start").value;
    info.end = document.getElementById("end").value;
    console.log(info)
}

function buttonPressed(id){
    document.getElementById(id).setAttribute("class", "buttonPresssed")
}

function toggleText() {
    var text = document.getElementById("appear")
    document.getElementById("appear1").style.display = "none";
    if (text.style.display === "none") {
        text.style.display = "contents";
    } else {
        text.style.display = "none";
    }
}

function toggleText1() {
    var text = document.getElementById("appear1")
    document.getElementById("appear").style.display = "none";
    if (text.style.display === "none") {
        text.style.display = "contents";
    } else {
        text.style.display = "none";
    }
}
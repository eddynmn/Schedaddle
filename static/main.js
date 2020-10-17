function sayHello() {
    let a = ""
    fetch('hello')
        .then(res => res.json())
        .then(data => {
            a = data.data;
            alert(a);
        })
 }
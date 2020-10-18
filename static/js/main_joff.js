var containers = document.querySelectorAll(".container");

class item {
  constructor(name, priority, duration) {
    this.createDiv(name, priority, duration);
  }

  createDiv(name, priority, duration) {
    // assigns name and time for task to task box
    let input = document.createElement("input");
    input.type = "text";
    // var taskTime = start.getHours() + ":" + start.getMinutes() + " - " end.getHours() + ":" + end.getMinutes();
    input.value = name; //+ " ~ " + taskTime;

    // prevents task from being edited
    input.disabled = true;

    // assigns priority to task box
    if (priority === "flex1") {
      input.classList.add("flex1");
    } else if (priority === "flex2") {
      input.classList.add("flex2");
    } else if (priority === "fixed1") {
      input.classList.add("fixed1");
    } else {
      input.classList.add("fixed2");
    }

    // adjusts height of task box based on task duration (longer tasks = longer boxes)
    var num = (duration / 60) * 80;
    var adjheight = num.toString() + "px";
    input.style.height = adjheight;

    /* creates due date text
    let dueDate = document.createElement("h4");
    dueDate.classList.add("dd");
    dueDate.value = "Due Date/Time: <br />" + due.getMonth() + " " + due.getDay() + ", " + due.getYear(); */

    // creates a new box for task
    let taskBox = document.createElement("div");
    taskBox.classList.add("container");

    // puts actual task in the box
    taskBox.appendChild(input);
    //taskBox.appendChild(dueDate);

    // decides whether the task box goes in the morning or afternoon
    if (priority === "flex1" || priority === "fixed1") {
      containers[0].appendChild(taskBox);
    } else {
      containers[1].appendChild(taskBox);
    }
  }
}

new item("English", "fixed2", 55);
new item("HW", "flex2", 120);
new item("Linear Algebra", "fixed2", 50);
new item("Laundry", "flex2", 20);

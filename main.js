var containers = document.querySelectorAll(".container");

class item {
  constructor(name, priority, start, end, duration) {
    this.createDiv(name, priority, start, end, duration);
  }

  createDiv(name, priority, start, end, duration) {
    // assigns name and time for task to task box
    let input = document.createElement("input");
    input.type = "text";
    input.value = name;

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
    var num = (duration / 60) * 100;
    var adjheight = num.toString() + "px";
    input.style.height = adjheight;

    // creates a new box for task
    let taskBox = document.createElement("div");
    taskBox.classList.add("container");

    // puts actual task in the box
    taskBox.appendChild(input);

    // decides whether the task box goes in the morning or afternoon
    if (priority === "flex1" || priority === "fixed1") {
      containers[0].appendChild(taskBox);
    } else {
      containers[1].appendChild(taskBox);
    }
  }
}

new item("Go for a run", "flex1", 900, 920, 20);
new item("English", "fixed1", 930, 1025, 55);
new item("Robojackets programming exercises", "flex1", 1030, 1100, 30);
new item("ECE 2020", "fixed1", 1100, 1215, 75);
new item("Lunch with friends", "fixed2", 1220, 1320, 60);
new item("Study for Linear Algebra", "flex2", 1345, 1430, 45);
new item("Receive package from post office", "flex2", 1440, 1510, 30);
new item("Linear Algebra exam", "fixed2", 1530, 1620, 50);
new item("Call parents", "flex2", 1625, 1640, 15);
new item("Play intramural volleyball game", "fixed2", 1650, 1740, 50);
new item("Get dinner", "fixed2", 1750, 1830, 40);

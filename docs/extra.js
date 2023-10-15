function toggle_click(button, id_str) {
    var block = document.getElementById(id_str);
    if (button.innerHTML == "Show the answer") {
      block.style.display = "block";
      button.innerHTML= "Hide the answer";
    } else {
      block.style.display = "none";
      button.innerHTML= "Show the answer";
    }
  }
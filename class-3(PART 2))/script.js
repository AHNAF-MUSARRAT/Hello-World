// DOM access
// What is DOM?
// DOM is a programming interface for HTML. It represents the page so that programs can change the document structure, style, and content.

// Access DOM elements
let dom_title = document.getElementById("dom-title");
dom_title.innerHTML = "Hello, This is DOM Magic!";

let dom_title_2 = document.getElementById("dom-title-2");
dom_title_2.style.backgroundColor = "blue";

// Changing image

let img1 = document.getElementById("img1");
let img2 = document.getElementById("img2");

function replace() {
  img1.style.display = "none";
  img2.src =
    "https://cldn.cdn-blackroll.com/image/upload/f_auto,q_auto,ar_1.5,c_fill,w_1400/oneworld-prod/assets/ergonomics_desktop_WEB.jpg?v=1611827054";
}

let canvas;
let classifier;
let synth;

function setup() {
  canvas = createCanvas(450, 350);
  canvas.parent("canvas-container");

  background("white");

  classifier = ml5.imageClassifier("DoodleNet", modelLoaded);

  synth = window.speechSynthesis;

  canvas.mouseReleased(classifyCanvas);
}

function modelLoaded() {
  console.log("DoodleNet Loaded Successfully!");
}

function classifyCanvas() {
  classifier.classify(canvas, gotResult);
}

function gotResult(error, results) {
  if (error) {
    console.error(error);
    return;
  }

  let label = results[0].label;
  let confidence = (results[0].confidence * 100).toFixed(2);

  document.getElementById("label").innerHTML = label;

  document.getElementById("accuracy").innerHTML = confidence + "%";

  // Speak only if confidence is above 85%
  if (confidence >= 85) {
    window.speechSynthesis.cancel();

    let speech = new SpeechSynthesisUtterance("I think it is " + label);

    synth.speak(speech);
  }
}

function draw() {
  strokeWeight(6);

  stroke(0);

  if (mouseIsPressed) {
    line(mouseX, mouseY, pmouseX, pmouseY);
  }
}

function clearCanvas() {
  background("white");

  document.getElementById("label").innerHTML = "Waiting...";

  document.getElementById("accuracy").innerHTML = "--%";

  window.speechSynthesis.cancel();
}

// Speech Recognition
let recognition = new webkitSpeechRecognition();

let textbox = document.getElementById("textbox");

let speech = window.speechSynthesis;

// Webcam settings
Webcam.set({
  width: 350,
  height: 280,
  image_format: "png",
  png_quality: 90,
});

Webcam.attach("#camera");

// Start listening
function start() {
  textbox.value = "Listening...";
  recognition.start();
}

// Voice result
recognition.onresult = function (event) {
  let command = event.results[0][0].transcript.toLowerCase();

  textbox.value = command;

  if (
    command.includes("selfie") ||
    command.includes("photo") ||
    command.includes("picture")
  ) {
    let msg = new SpeechSynthesisUtterance(
      "Taking your selfie in five seconds",
    );

    speech.speak(msg);

    setTimeout(function () {
      takeSelfie();
    }, 5000);
  } else {
    let msg = new SpeechSynthesisUtterance("Please say take my selfie.");

    speech.speak(msg);
  }
};

// Capture image
function takeSelfie() {
  Webcam.snap(function (data_uri) {
    document.getElementById("result").innerHTML =
      `<img id="selfie" src="${data_uri}" width="350">`;

    document.getElementById("link").href = data_uri;
  });
}

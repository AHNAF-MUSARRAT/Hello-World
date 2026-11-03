const output = document.getElementById("output");
const statusText = document.getElementById("status");

function startRecognition() {
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    alert("Speech Recognition is not supported in this browser.");
    return;
  }

  const recognition = new SpeechRecognition();

  recognition.lang = "en-US";
  recognition.continuous = true;
  recognition.interimResults = true;

  recognition.start();
  statusText.innerHTML = "🎙 Listening...";

  recognition.onresult = function (event) {
    let transcript = "";

    for (let i = 0; i < event.results.length; i++) {
      transcript += event.results[i][0].transcript;
    }

    output.value = transcript;
  };

  recognition.onend = function () {
    statusText.innerHTML = "Stopped Listening";
  };

  recognition.onerror = function () {
    statusText.innerHTML = "Error Occurred";
  };
}

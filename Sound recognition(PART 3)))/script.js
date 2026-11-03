function start() {
  navigator.mediaDevices.getUserMedia({ audio: true });

  let classifier = ml5.soundClassifier(
    "https://teachablemachine.withgoogle.com/models/bb48To9iY/model.json",
    modelReady,
  );

  function modelReady() {
    console.log("Model Loaded");

    classifier.classify(gotResult);
  }
}

function gotResult(error, results) {
  if (error) {
    console.error(error);
    return;
  }

  let label = results[0].label;
  let confidence = results[0].confidence * 100;

  if (confidence >= 90) {
    document.getElementById("result-label").innerHTML = label;

    document.getElementById("result-confidence").innerHTML =
      "Confidence : " + confidence.toFixed(2) + "%";
  }

  let cars = ["lamborghini", "ferrari", "gtr", "bmw", "supra", "porsche"];

  cars.forEach(function (car) {
    document.getElementById(car).parentElement.classList.remove("active");
  });

  if (label == "Lamborghini") {
    document
      .getElementById("lamborghini")
      .parentElement.classList.add("active");
  } else if (label == "Ferrari") {
    document.getElementById("ferrari").parentElement.classList.add("active");
  } else if (label == "GTR") {
    document.getElementById("gtr").parentElement.classList.add("active");
  } else if (label == "BMW") {
    document.getElementById("bmw").parentElement.classList.add("active");
  } else if (label == "Supra") {
    document.getElementById("supra").parentElement.classList.add("active");
  } else if (label == "Porsche") {
    document.getElementById("porsche").parentElement.classList.add("active");
  }
}

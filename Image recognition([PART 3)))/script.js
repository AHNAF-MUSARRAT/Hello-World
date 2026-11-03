// ======================================
// AI Image Recognition using ML5.js
// Teachable Machine Model
// ======================================

// Load the trained Teachable Machine model
let classifier = ml5.imageClassifier(
  "https://teachablemachine.withgoogle.com/models/WtadlvMro/model.json",
  modelLoaded,
);

// Runs after the model loads successfully
function modelLoaded() {
  console.log("✅ AI Model Loaded Successfully!");
}

// Configure the webcam
Webcam.set({
  width: 350,
  height: 300,
  image_format: "png",
  png_quality: 90,
});

// Attach the webcam to the HTML div
Webcam.attach("#camera");

// Capture an image
function takeSnapshot() {
  Webcam.snap(function (data_uri) {
    // Show the captured image
    document.getElementById("result").innerHTML =
      `<img id="capturedImage" src="${data_uri}" class="img-fluid rounded shadow">`;

    // Automatically recognize the image
    classifyImage();
  });
}

// Classify the captured image
function classifyImage() {
  const image = document.getElementById("capturedImage");

  if (!image) {
    alert("Please capture an image first!");
    return;
  }

  classifier.classify(image, gotResult);
}

// Display prediction
function gotResult(error, results) {
  if (error) {
    console.error(error);
    alert("Something went wrong while recognizing the image.");
    return;
  }

  // Display the predicted object
  document.getElementById("objectName").innerHTML = results[0].label;

  // Display confidence score
  document.getElementById("confidence").innerHTML =
    "Confidence: " + (results[0].confidence * 100).toFixed(2) + "%";

  console.log(results);
}

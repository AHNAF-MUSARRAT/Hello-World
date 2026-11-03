const imageUpload = document.getElementById("image-upload");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const output = document.getElementById("output");
const fileName = document.getElementById("file-name");

canvas.width = 600;
canvas.height = 400;

let model;

cocoSsd.load().then(function(loadedModel){

    model = loadedModel;

    output.innerHTML = "AI model is ready ✓";

}).catch(function(){

    output.innerHTML = "Model could not load";

});


imageUpload.addEventListener("change", function(event){

    const file = event.target.files[0];

    if(!file) return;

    fileName.innerHTML = file.name;

    const image = new Image();
    const reader = new FileReader();

    reader.onload = function(){

        image.src = reader.result;

        image.onload = function(){

            ctx.clearRect(0,0,canvas.width,canvas.height);

            ctx.drawImage(
                image,
                0,
                0,
                canvas.width,
                canvas.height
            );

            detectObjects(image);

        };

    };

    reader.readAsDataURL(file);

});


function detectObjects(image){

    if(!model){
        output.innerHTML = "Please wait for the AI model...";
        return;
    }

    output.innerHTML = "Scanning image...";

    model.detect(image).then(function(predictions){

        output.innerHTML =
            predictions.length + " object(s) detected";

        const scaleX = canvas.width / image.width;
        const scaleY = canvas.height / image.height;

        predictions.forEach(function(prediction){

            const [x,y,width,height] = prediction.bbox;

            const newX = x * scaleX;
            const newY = y * scaleY;
            const newWidth = width * scaleX;
            const newHeight = height * scaleY;

            ctx.strokeStyle = "#00a6b4";
            ctx.lineWidth = 3;

            ctx.strokeRect(
                newX,
                newY,
                newWidth,
                newHeight
            );

            const confidence =
                (prediction.score * 100).toFixed(1);

            ctx.fillStyle = "#00a6b4";

            ctx.font = "bold 16px Arial";

            ctx.fillText(
                prediction.class + " " + confidence + "%",
                newX,
                newY > 20 ? newY - 7 : newY + 20
            );

        });

    });

}
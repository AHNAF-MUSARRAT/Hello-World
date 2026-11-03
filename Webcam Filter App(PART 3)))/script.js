const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const filterText = document.getElementById("currentFilter");
const buttons = document.querySelectorAll(".filter-btn");

let currentFilter = "none";

const filters = {
    none: "none",
    grayscale: "grayscale(100%)",
    sepia: "sepia(100%)",
    invert: "invert(100%)",
    blur: "blur(5px)",
    brightness: "brightness(150%)",
    contrast: "contrast(200%)",
    hue: "hue-rotate(90deg)"
};

buttons.forEach(function(button){

    button.addEventListener("click",function(){

        buttons.forEach(function(btn){
            btn.classList.remove("active");
        });

        this.classList.add("active");

        currentFilter = this.dataset.filter;

        filterText.innerHTML = "Current Filter : " + this.innerText;

    });

});

function startWebcam(){

    navigator.mediaDevices.getUserMedia({video:true})

    .then(function(stream){

        const video = document.createElement("video");

        video.srcObject = stream;

        video.play();

        video.onloadedmetadata = function(){

            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;

            draw(video);

        };

    })

    .catch(function(){

        alert("Please allow webcam permission.");

    });

}

function draw(video){

    ctx.filter = filters[currentFilter];

    ctx.drawImage(video,0,0,canvas.width,canvas.height);

    requestAnimationFrame(function(){

        draw(video);

    });

}

startWebcam();
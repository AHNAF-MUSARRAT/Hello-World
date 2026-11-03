let questions = [

    {
        question: "Which company makes the 911?",
        answers: [
            "Ferrari",
            "Porsche",
            "Toyota",
            "Ford"
        ],
        correct: 1
    },

    {
        question: "What does EV stand for?",
        answers: [
            "Engine Vehicle",
            "Electric Vehicle",
            "Extra Vehicle",
            "Energy Vehicle"
        ],
        correct: 1
    },

    {
        question: "Which system helps prevent wheel lock during braking?",
        answers: [
            "GPS",
            "ABS",
            "AC",
            "USB"
        ],
        correct: 1
    },

    {
        question: "Which country is Ferrari from?",
        answers: [
            "Germany",
            "Japan",
            "Italy",
            "USA"
        ],
        correct: 2
    },

    {
        question: "What is Formula 1?",
        answers: [
            "A racing championship",
            "A car company",
            "A type of fuel",
            "A car model"
        ],
        correct: 0
    }

];

let currentQuestion = 0;
let score = 0;


function loadQuestion() {

    let q = questions[currentQuestion];

    document.getElementById("question").innerText =
        q.question;

    document.getElementById("answer0").innerText =
        q.answers[0];

    document.getElementById("answer1").innerText =
        q.answers[1];

    document.getElementById("answer2").innerText =
        q.answers[2];

    document.getElementById("answer3").innerText =
        q.answers[3];

    document.getElementById("result").innerText = "";

    document.getElementById("next").style.display = "none";
}


function checkAnswer(answer) {

    let correctAnswer =
        questions[currentQuestion].correct;

    if (answer == correctAnswer) {

        score++;

        document.getElementById("result").innerText =
            "Correct! 👍";

    } else {

        document.getElementById("result").innerText =
            "Wrong answer!";

    }

    document.getElementById("next").style.display =
        "inline-block";
}


function nextQuestion() {

    currentQuestion++;

    if (currentQuestion < questions.length) {

        loadQuestion();

    } else {

        document.getElementById("quiz").innerHTML =
            "<h2>Quiz Complete!</h2>" +
            "<p>You scored " + score +
            " out of " + questions.length + ".</p>";

        document.getElementById("result").innerText =
            "Thanks for playing!";

        document.getElementById("next").style.display =
            "none";
    }
}


loadQuestion();
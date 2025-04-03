const streak = document.getElementById("streak");
const streakbox = document.getElementsByClassName("streakbox")[0];
const input = document.getElementById("answer-field");
const bgBlur = document.getElementById("blur");
const question = document.getElementById("finalQuestion");

const coeffs = document.getElementsByClassName("coeff");
const answerInputs = document.getElementsByClassName("answer-input");

const polynomial = document.getElementById("poly").innerText;

window.onload = () => {
  setStreak();
  updateQuestion();
};

function updateQuestion() {
  let a = document.getElementById("x1").value;
  let b = document.getElementById("x2").value;

  a = a ? a : String.raw`x_1`;
  b = b ? b : String.raw`x_2`;

  question.innerHTML =
    String.raw`\[ \int_{${a}}^{${b}}` + polynomial + String.raw`\,dx = \]`;

  MathJax.Hub.Typeset();
}

function setStreak() {
  let currentStreak = getCookie("streak");
  if (currentStreak) {
    streak.innerText = currentStreak;
  }
  let hasCompleted = getCookie("hasCompleted");
  if (hasCompleted) {
    streakbox.classList.add("streak");
  }
}

function closePopUp(e) {
  e.classList.remove("shown");
  bgBlur.classList.remove("active");
}

popups = document.getElementsByClassName("pop");
for (let i = 0; i < coeffs.length; i++) {
  coeffs[i].addEventListener("mouseup", () => {
    coeffs[i].classList.remove("valid");
    coeffs[i].classList.remove("invalid");
    popups[i].classList.add("shown");
    bgBlur.classList.add("active");
  });
  closeBtn = popups[i].querySelector("#closePop");
  closeBtn.addEventListener("mouseup", () => {
    closePopUp(popups[i]);
  });
  sendBtn = popups[i].querySelector("#sendBtn");
  sendBtn.addEventListener("mouseup", () => {
    closePopUp(popups[i]);
    coeffs[i].innerText = popups[i].querySelector("#pop-answer").value;
  });
}

// Send POST requests
async function sendPostRequest(data) {
  try {
    const response = await fetch(window.location.origin + "/validate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }

    const responseData = await response.json();
    return responseData;
  } catch (error) {
    console.error("Error:", error);
    return null;
  }
}

// Validate the answers
async function validate() {
  clearValidation();
  let answers = [
    coeffs[0].innerText,
    coeffs[1].innerText,
    coeffs[2].innerText,
    answerInputs[0].value,
    answerInputs[1].value,
    answerInputs[2].value,
  ];

  const response = await sendPostRequest({ answers: answers });

  if (response) {
    if (response[0]) {
      coeffs[0].classList.add("valid");
    } else {
      coeffs[0].classList.add("invalid");
    }
    if (response[1]) {
      coeffs[1].classList.add("valid");
    } else {
      coeffs[1].classList.add("invalid");
    }
    if (response[2]) {
      coeffs[2].classList.add("valid");
    } else {
      coeffs[2].classList.add("invalid");
    }
    if (response[3]) {
      answerInputs[0].classList.add("valid");
    } else {
      answerInputs[0].classList.add("invalid");
    }
    if (response[4]) {
      answerInputs[1].classList.add("valid");
    } else {
      answerInputs[1].classList.add("invalid");
    }
    if (response[5]) {
      answerInputs[2].classList.add("valid");
    } else {
      answerInputs[2].classList.add("invalid");
    }
  } else {
    alert("An error occurred while validating the answers");
  }

  const allTrue = response.every((element) => element === true);
  if (allTrue) {
    streak.classList.add("streak");
    increaseStreak();
  }
  setTimeout(clearValidation, 2000);
}

function clearValidation() {
  for (let i = 0; i < coeffs.length; i++) {
    coeffs[i].classList.remove("valid");
    coeffs[i].classList.remove("invalid");
  }
  for (let i = 0; i < answerInputs.length; i++) {
    answerInputs[i].classList.remove("valid");
    answerInputs[i].classList.remove("invalid");
  }
}

function increaseStreak() {
  if (getCookie("hasCompleted")) {
    alert(
      "You have already completed the challenge for today!\nSee you tomorrow!"
    );
    return;
  }

  let currentStreak = getCookie("streak");
  let streak = currentStreak ? parseInt(currentStreak) + 1 : 1;

  // Calculate the expiration date 24 hours from now
  let date = new Date();

  date.setTime(date.getTime() + 24 * 60 * 60 * 1000);
  let streakExpires = "expires=" + date.toUTCString();

  date.setHours(24, 0, 0, 0); // Set to 00:00 of the next day
  let completionExpires = "expires=" + date.toUTCString();

  document.cookie = `streak=${streak}; ${streakExpires}; path=/`;
  document.cookie = `hasCompleted=true; ${completionExpires}; path=/`;
  setStreak();
}

function getCookie(name) {
  const cookieArr = document.cookie.split(";");

  for (let i = 0; i < cookieArr.length; i++) {
    const cookiePair = cookieArr[i].split("=");

    if (name === cookiePair[0].trim()) {
      return decodeURIComponent(cookiePair[1]);
    }
  }

  return null;
}

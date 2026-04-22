// ==============================
// AUDIO SETUP
// ==============================

let typeSound = new Audio("sounds/type.mp3");
typeSound.loop = true;
typeSound.volume = 0.3;

let bgMusic = new Audio("sounds/horror_ringtone.mp3");
bgMusic.loop = true;
bgMusic.volume = 0.2;

document.body.addEventListener("click", () => {
    bgMusic.play();

    typeSound.play().then(() => {
        typeSound.pause();
        typeSound.currentTime = 0;
    });
}, { once: true });


// ==============================
// INITIAL LOAD
// ==============================

window.addEventListener("DOMContentLoaded", async () => {
    setupButtons();
    setupExitButton(); // 🔥 FIXED

    //let cases = await window.pywebview.api.get_cases();
    let res = await fetch("/get_cases");
let cases = await res.json();
    let list = document.getElementById("caseList");
    list.innerHTML = "";

    let descriptions = [
        "Locked room murder in a stormy mansion",
        "Murder inside a moving train at midnight",
        "Death inside a haunted abandoned hospital",
        "Poisoning at a high-class dinner party",
        "Brutal hostel murder among students"
    ];

    cases.forEach((c, index) => {

        let btn = document.createElement("div");
        btn.className = "case-btn";

        btn.innerHTML = `
            <div><b>${c}</b></div>
            <div class="case-desc">${descriptions[index]}</div>
        `;

        btn.onclick = () => startGame(index);

        list.appendChild(btn);
    });

});


// ==============================
// EXIT SYSTEM (FIXED)
// ==============================

function setupExitButton() {
    let exitBtn = document.getElementById("exitBtn");

    if (exitBtn) {
        exitBtn.onclick = showExitDialog;
    }
}

function showExitDialog() {

    let div = document.createElement("div");

    div.innerHTML = `
        <div style="
            position:fixed;
            top:0;
            left:0;
            width:100vw;
            height:100vh;
            background: rgba(0,0,0,0.95);
            display:flex;
            align-items:center;
            justify-content:center;
            z-index:9999;
        ">
            <div style="
                border:1px solid red;
                padding:30px;
                background:black;
                color:red;
                text-align:center;
                width:400px;
                box-shadow:0 0 20px red;
            ">
                <h2>GAME ABANDONED</h2>
                <p>The darkness was too much...</p>

                <button id="exitConfirm" style="
                    margin-top:15px;
                    padding:10px;
                    background:red;
                    border:none;
                    color:black;
                    cursor:pointer;
                ">Return to Cases</button>
            </div>
        </div>
    `;

    document.body.appendChild(div);

    document.getElementById("exitConfirm").onclick = () => {
        resetGame(); // 🔥 PROPER RESET (no reload)
        div.remove();
    };
}


// ==============================
// GAME START / RESET
// ==============================

async function startGame(index) {
    try {
        console.log("Clicked case:", index);

        let res = await fetch("/select_case", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ index })
        });

        let data = await res.json();
        let story = data.story;

        document.getElementById("caseMenu").style.display = "none";

document.querySelector(".header").style.display = "block";
document.querySelector(".container").style.display = "flex";

        document.getElementById("story").innerHTML = "";
        document.getElementById("outputBox").innerHTML = "";
        document.getElementById("clueBox").innerHTML = "";

        typeWriter("story", story);

        await loadSuspects();

    } catch (e) {
        console.error("ERROR:", e);
    }
}


function resetGame() {
    document.getElementById("story").innerHTML = "";
    document.getElementById("outputBox").innerHTML = "";
    document.getElementById("clueBox").innerHTML = "";

    document.getElementById("caseMenu").style.display = "flex";

    document.querySelector(".header").style.display = "none";
    document.querySelector(".container").style.display = "none";
}


// ==============================
// SUSPECT + QUESTIONS SYSTEM
// ==============================

async function loadSuspects() {
   // let suspects = await window.pywebview.api.get_suspects();
    let res = await fetch("/get_suspects");
let suspects = await res.json();



    let dropdown = document.getElementById("suspects");
    dropdown.innerHTML = "";

    suspects.forEach(s => {
        let opt = document.createElement("option");
        opt.value = s;
        opt.textContent = s;
        dropdown.appendChild(opt);
    });

    if (suspects.length > 0) {
        await loadQuestions(suspects[0]);
    }

    dropdown.onchange = async () => {
        await loadQuestions(dropdown.value);
    };
}

async function loadQuestions(suspectName) {
    //l
    // et questions = await window.pywebview.api.get_questions(suspectName);
    let res = await fetch("/get_questions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ suspect: suspectName })
});

let questions = await res.json();


    let qDropdown = document.getElementById("questions");
    qDropdown.innerHTML = "";

    questions.forEach(q => {
        let opt = document.createElement("option");
        opt.value = q;
        opt.textContent = q;
        qDropdown.appendChild(opt);
    });
}


// ==============================
// TYPEWRITER
// ==============================

function typeWriter(id, text) {
    let el = document.getElementById(id);
    el.innerHTML = "";

    let i = 0;

    typeSound.currentTime = 0;
    typeSound.play();

    function typing() {
        if (i < text.length) {

            let char = text.charAt(i);
            el.innerHTML += char;
            i++;

            let speed = Math.random() * 40 + 20;

            if (char === "." || char === "," || char === "\n") {
                speed += 200;
            }

            if (Math.random() < 0.05) {
                speed += 300;
            }

            setTimeout(typing, speed);

        } else {
            typeSound.pause();
            typeSound.currentTime = 0;
        }
    }

    typing();
}


// ==============================
// INTERROGATION
// ==============================

async function ask() {
    let s = document.getElementById("suspects").value;
    let q = document.getElementById("questions").value;

    //let res = await window.pywebview.api.ask(s, q);
    let res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ suspect: s, question: q })
});

let data = await res.json();
let answer = data.answer;

    let box = document.getElementById("outputBox");
    box.innerHTML += `<div style="color:#00ff9f">[${s}]</div> ${answer}<br><br>`;
    box.scrollTop = box.scrollHeight;
}


// ==============================
// ACCUSATION
// ==============================
// ==============================
// ACCUSATION
// ==============================

async function accuse() {
    let s = document.getElementById("suspects").value;
    //let result = await window.pywebview.api.accuse(s);
   let res = await fetch("/accuse", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ suspect: s })
});

let data = await res.json();
let result = data.result;

    if (result) {
        showWinScreen();
    } else {
        showLoseScreen();
    }
}

// ==============================
// WIN SCREEN
// ==============================

function showWinScreen() {

    let win = document.createElement("div");

    win.innerHTML = `
        <div style="
            position:fixed;
            top:0;
            left:0;
            width:100%;
            height:100%;
            background:black;
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            color:lime;
            font-size:32px;
            z-index:9999;
            text-shadow: 0 0 15px lime;
        ">
            🕵️ WELL PLAYED DETECTIVE 🕵️
            <p style="font-size:16px;color:#aaa;">Justice has been served...</p>
        </div>
    `;

    document.body.appendChild(win);

    setTimeout(() => {
        win.remove();
        resetGame(); // 🔥 go back to menu cleanly
    }, 3000);
}

// ==============================
// LOSE SCREEN
// ==============================

function showLoseScreen() {

    let div = document.createElement("div");

    div.innerHTML = `
        <div style="
            position:fixed;
            top:0;
            left:0;
            width:100%;
            height:100%;
            background: linear-gradient(black, darkred);
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            color:red;
            font-size:32px;
            z-index:9999;
            text-shadow: 0 0 15px red;
        ">
            ☠ YOU CHOSE POORLY ☠

            <p style="font-size:16px;color:#aaa;margin-top:10px;">
                The killer smiles in the shadows...
            </p>

            <div style="margin-top:25px;">
                <button id="retryBtn" style="
                    padding:10px;
                    margin-right:10px;
                    background:black;
                    color:red;
                    border:1px solid red;
                    cursor:pointer;
                ">Continue Investigation</button>

                <button id="exitGameBtn" style="
                    padding:10px;
                    background:red;
                    color:black;
                    border:none;
                    cursor:pointer;
                ">Abandon Case</button>
            </div>
        </div>
    `;

    // 🔥 quick red flash effect
    document.body.style.background = "darkred";
    setTimeout(() => {
        document.body.style.background = "";
    }, 150);

    document.body.appendChild(div);

    // 🔥 attach actions AFTER render
    document.getElementById("retryBtn").onclick = () => {
        div.remove(); // continue game
    };

    document.getElementById("exitGameBtn").onclick = () => {
        div.remove();
        resetGame(); // go to menu properly (no reload)
    };
}
// ==============================
// CLUE SYSTEM
// ==============================

function setupButtons() {
    document.querySelectorAll(".fake").forEach(btn => {
        btn.onclick = fakeEvent;
    });

    let clueBtn = document.getElementById("clueBtn");

    if (clueBtn) {
        clueBtn.onclick = async () => {
            let box = document.getElementById("clueBox");
            let random = Math.random();

            if (random < 0.4) {
                triggerHorror(box);
            } else {
                //let clue = await window.pywebview.api.get_clue();
                let res = await fetch("/get_clue");
let data = await res.json();
let clue = data.clue;
                typeClue(box, " " + clue);
            }
        };
    }
}

function typeClue(box, text) {
    let div = document.createElement("div");
    box.appendChild(div);

    let i = 0;

    function typing() {
        if (i < text.length) {
            div.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, 20);
        }
    }

    typing();
}

function triggerHorror(box) {

    // 💀 horror messages
    let horrors = [
        "Something is behind you...",
        "You hear scratching inside the walls...",
        "That clue felt wrong.",
        "A cold breath touches your neck.",
        "This was not meant to be found."
    ];

    let msg = horrors[Math.floor(Math.random() * horrors.length)];

    typeClue(box, "⚠ " + msg);

    // =========================
    // 🩸 BLOOD SPLASH
    // =========================
    let img = document.createElement("img");
    img.src = "assets/blood.jpeg";   // ✅ make sure file exists

    img.style.position = "fixed";
    img.style.top = "0";
    img.style.left = "0";
    img.style.width = "100%";
    img.style.opacity = "0.8";
    img.style.zIndex = "9999";
    img.style.pointerEvents = "none";

    document.body.appendChild(img);

    setTimeout(() => img.remove(), 400);

    // =========================
    // 📳 SCREEN SHAKE
    // =========================
    document.body.classList.add("shake");

    setTimeout(() => {
        document.body.classList.remove("shake");
    }, 400);

    // =========================
    // ⚡ FLASH EFFECT
    // =========================
    document.body.style.filter = "brightness(2)";
    setTimeout(() => {
        document.body.style.filter = "brightness(1)";
    }, 100);

    // =========================
    // 🔊 SOUND (OPTIONAL)
    // =========================
    /*
    let scream = new Audio("sounds/scream.mp3");
    scream.volume = 0.7;
    scream.play();
    */
}
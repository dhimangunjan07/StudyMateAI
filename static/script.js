// =========================
// StudyMateAI Script
// =========================

// Auto Scroll Chat

window.onload = function () {

    const chatBox = document.getElementById("chatBox");

    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight;
    }

};


// Clear Chat

function clearChat() {

    const chatBox = document.getElementById("chatBox");

    if (chatBox) {

        chatBox.innerHTML = "";

    }

}


// Press Enter to Submit

const input = document.querySelector('input[name="question"]');

if (input) {

    input.addEventListener("keypress", function (e) {

        if (e.key === "Enter") {

            e.preventDefault();

            this.form.submit();

        }

    });

}


// Loading Animation

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function () {

        const btn = document.querySelector(".input-area button");

        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';

        btn.disabled = true;

    });

}


// Copy Code Button

document.querySelectorAll("pre").forEach((block) => {

    const button = document.createElement("button");

    button.innerHTML = "📋 Copy";

    button.style.marginBottom = "10px";
    button.style.padding = "8px 15px";
    button.style.border = "none";
    button.style.borderRadius = "8px";
    button.style.cursor = "pointer";
    button.style.background = "#7c3aed";
    button.style.color = "white";

    button.onclick = function () {

        navigator.clipboard.writeText(block.innerText);

        button.innerHTML = "✅ Copied";

        setTimeout(() => {

            button.innerHTML = "📋 Copy";

        }, 1500);

    };

    block.parentNode.insertBefore(button, block);

});
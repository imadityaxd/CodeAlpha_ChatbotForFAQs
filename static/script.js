// Show greeting when page loads
window.onload = function () {
  const chatBox = document.getElementById("chatBox");
  chatBox.innerHTML += `<div><strong>Gemini:</strong> Hello! I’m your coding assistant. Ask me anything or try one of the questions above! 👨‍💻</div>`;
};

function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chatBox");
  chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
  input.value = "";

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  })
  .then(res => res.json())
  .then(data => {
    chatBox.innerHTML += `<div><strong>Gemini:</strong> ${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}

function sendPrebuilt(question) {
  document.getElementById("userInput").value = question;
  sendMessage();
}

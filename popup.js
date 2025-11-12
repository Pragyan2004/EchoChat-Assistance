let productInfo = { title: "", reviews: [] };

document.addEventListener("DOMContentLoaded", () => {
  const summarizeBtn = document.getElementById("summarize-btn");
  const analyzeBtn = document.getElementById("analyze-btn");
  const compareBtn = document.getElementById("compare-btn");
  const prosconsBtn = document.getElementById("proscons-btn");
  const sendBtn = document.getElementById("send-btn");
  const userInput = document.getElementById("user-input");
  const chatLog = document.getElementById("chat-log");

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "getProductInfo" }, (response) => {
      if (response) {
        productInfo = response;
        document.getElementById("product-title").innerText = productInfo.title;
        document.getElementById("product-description").innerText = productInfo.description;
      }
    });
  });

  function addMessage(sender, message) {
    const div = document.createElement("div");
    div.className = sender.toLowerCase();
    div.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatLog.appendChild(div);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function postData(url, payload, key, errorMsg) {
    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then(r => r.json())
      .then(d => addMessage("Bot", d[key] || `No ${key}.`))
      .catch(() => addMessage("Bot", errorMsg));
  }

  summarizeBtn.addEventListener("click", () => {
    postData("http://127.0.0.1:5000/summarize", { reviews: productInfo.reviews }, "summary", "Error summarizing reviews.");
  });

  analyzeBtn.addEventListener("click", () => {
    postData("http://127.0.0.1:5000/analyze", { reviews: productInfo.reviews }, "analysis", "Error analyzing reviews.");
  });

  prosconsBtn.addEventListener("click", () => {
    postData("http://127.0.0.1:5000/proscons", { reviews: productInfo.reviews }, "proscons", "Error extracting pros & cons.");
  });

  compareBtn.addEventListener("click", () => {
    const other = prompt("Enter another product name to compare:");
    if (!other) return;
    postData("http://127.0.0.1:5000/compare", { product1: productInfo.title, product2: other }, "comparison", "Error comparing products.");
  });

  sendBtn.addEventListener("click", () => {
    const msg = userInput.value.trim();
    if (!msg) return;
    addMessage("You", msg);
    userInput.value = "";
    postData("http://127.0.0.1:5000/ask", { title: productInfo.title, description: productInfo.description, reviews: productInfo.reviews, question: msg }, "answer", "Error sending message.");
  });
});

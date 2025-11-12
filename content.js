function getProductInfo() {
  const titleEl = document.querySelector("#productTitle") || document.querySelector("h1");
  const descEl = document.querySelector("#feature-bullets") || document.querySelector("#productDescription");
  const reviewEls = document.querySelectorAll(".review-text-content span");

  return {
    title: titleEl ? titleEl.innerText.trim() : "Unknown Product",
    description: descEl ? descEl.innerText.trim() : "",
    reviews: Array.from(reviewEls).map(el => el.innerText.trim())
  };
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getProductInfo") {
    sendResponse(getProductInfo());
  }
});

document.getElementById("openButton").addEventListener("click", () => {
  browser.tabs.create({
    url: browser.runtime.getURL("upload.html")
  });
});
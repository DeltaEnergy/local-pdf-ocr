document.getElementById("ocrButton").addEventListener("click", async () => {
  const input = document.getElementById("pdfInput");
  const status = document.getElementById("status");
  const quality = document.getElementById("qualitySelect").value;

  if (!input.files.length) {
    status.textContent = "Choose a PDF first.";
    return;
  }

  const file = input.files[0];

  if (!file.name.toLowerCase().endsWith(".pdf")) {
    status.textContent = "Only PDF files are supported.";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  status.textContent =
    quality === "high"
      ? "Creating high-quality searchable PDF locally...\nThis may take a while."
      : "Creating fast searchable PDF locally...";

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/ocr-searchable-pdf?quality=${quality}`,
      {
        method: "POST",
        body: formData
      }
    );

    if (!response.ok) {
      status.textContent = "OCR failed. Check the backend window for the error.";
      return;
    }

    const blob = await response.blob();
    const downloadUrl = URL.createObjectURL(blob);

    const cleanName = file.name.replace(/\.pdf$/i, "");
    const a = document.createElement("a");

    a.href = downloadUrl;
    a.download = cleanName + "_searchable.pdf";

    document.body.appendChild(a);
    a.click();
    a.remove();

    URL.revokeObjectURL(downloadUrl);

    status.textContent = "Done. Searchable PDF downloaded.";
  } catch (error) {
    status.textContent =
      "Could not connect to backend.\n\nStart it by double-clicking start_backend.bat.";
  }
});
document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("audioFile");
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const res = await fetch("/upload-audio", {
    method: "POST",
    body: formData
  });
  const data = await res.json();

  document.getElementById("output").innerHTML = `
    <h3>Transcript:</h3>
    <p>${data?.transcript}</p>
    <h3>Insights:</h3>
    <p>${data?.insights}</p>
  `;
});

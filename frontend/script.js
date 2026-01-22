function uploadImageAndDetect() {
    const input = document.getElementById("imageInput");
    const file = input.files[0];
  
    if (!file) {
      alert("Please upload an image first!");
      return;
    }
  
    const formData = new FormData();
    formData.append("image", file);
  
    fetch("http://localhost:5000/detect", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        document.getElementById("resultImg").src = `data:image/jpeg;base64,${data.image}`;
        document.getElementById("freeSlots").innerText = `Free Slots: ${data.free_slots}`;
      })
      .catch((err) => {
        console.error("Detection failed:", err);
      });
  }
  
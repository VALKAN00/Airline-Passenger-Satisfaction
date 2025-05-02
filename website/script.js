document.getElementById("satisfaction-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = isNaN(value) ? value : Number(value);
    });
  
    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", data, {
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      document.getElementById("result").innerText = `Prediction: ${response.data.satisfaction}`;
    } catch (error) {
      document.getElementById("result").innerText = "Error contacting the server.";
      console.error("Prediction Error:", error);
    }
  });
  
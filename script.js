function predictStock() {
    let stock = document.getElementById("stock").value;
    let open = parseFloat(document.getElementById("open").value);
    let high = parseFloat(document.getElementById("high").value);
    let low = parseFloat(document.getElementById("low").value);
    let volume = parseFloat(document.getElementById("volume").value);

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ stock, open, high, low, volume })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerHTML = "Error: " + data.error;
        } else {
            document.getElementById("result").innerHTML = data.percentage_change + "%";
        }
    })
    .catch(error => console.error("Error:", error));
}
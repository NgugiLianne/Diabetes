document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form data
    const formData = new FormData(this);

    // Convert form data to JSON object
    const jsonData = {};
    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });

    // Send POST request to Flask server
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction-result').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => console.error('Error:', error));
});

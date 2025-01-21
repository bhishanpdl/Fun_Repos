async function rollDice(section) {
    const gif = document.getElementById("dice-gif");
    const resultText = document.getElementById("result");
    resultText.textContent = ""; // Clear previous result
    gif.hidden = false; // Show dice rolling gif

    // Simulate dice rolling effect
    setTimeout(async () => {
        const response = await fetch(`/roll/${section}`);
        const data = await response.json();
        gif.hidden = true; // Hide dice gif
        resultText.textContent = `${data.section}: ${data.result}`;
    }, 2000); // Wait 2 seconds for effect
}

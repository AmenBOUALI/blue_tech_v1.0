document.getElementById("analyze").addEventListener("click", async () => {
    const password = document.getElementById("password").value;
    const result = document.getElementById("result");

    result.textContent = "Analyzing...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ password })
        });

        if (!response.ok) {
            throw new Error("API error: " + response.status);
        }

        const data = await response.json();

        result.innerHTML = `
            <h3>Security Report</h3>
            <p>Score: ${data.score}/100</p>
            <p>Level: ${data.level}</p>
            <ul>
                ${data.recommendations.map(item => `<li>${item}</li>`).join("")}
            </ul>
        `;

    } catch (error) {
        result.textContent = "Error: " + error.message;
        console.error(error);
    }
});
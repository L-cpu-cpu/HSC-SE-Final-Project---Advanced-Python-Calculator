const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

document.getElementById("saveVarForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const varName = formData.get("varName");

    fetch("/save-variable", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": csrfToken
        }
    })
    .then(res => res.text())
    .then(data => {
        document.getElementById("saveStatusMsg").textContent = "Saved result to variable!";

        // Update dropdown label and value for all matching options
        const resultValue = document.getElementById("answerValue").textContent.trim();
        const dropdown = document.querySelector("select[name='varName']");
        Array.from(dropdown.options).forEach(opt => {
            if (opt.value === varName) {
                opt.textContent = `${varName} = ${resultValue}`;
            }
        });
    });
});

document.getElementById("saveResultForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    fetch("/save-result", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": csrfToken
        }
    })
    .then(res => res.text())
    .then(data => {
        console.log("Server response:", data);
        document.getElementById("saveStatusMsg").textContent = data === "Success" ? "Saved result!" : "Failed to save result.";
    });
});
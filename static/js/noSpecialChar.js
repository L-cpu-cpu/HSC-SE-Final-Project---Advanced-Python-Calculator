document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

    function handleFormSubmit(event) {
        const form = event.target;
        const inputs = form.querySelectorAll('input[name="dynamicInput"], input[name="input"], input[name^="x"], input[name^="y"]');
        const forbiddenChars = /[<>'";]/;
        let invalidInput = false;

        // Remove any existing alert
        const existingAlert = form.querySelector(".alert-box");
        if (existingAlert) existingAlert.remove();

        inputs.forEach(input => {
            if (forbiddenChars.test(input.value)) {
                invalidInput = true;
                input.value = "";
            }
        });

        if (invalidInput) {
            event.preventDefault(); // block the form submission
            const alertBox = document.createElement("div");
            alertBox.textContent = "Invalid characters detected. Please avoid using <, >, ', \", or ;.";
            alertBox.style.color = "red";
            alertBox.style.marginTop = "10px";
            alertBox.classList.add("alert-box");
            form.appendChild(alertBox);
        }
    }

    forms.forEach(form => {
        form.addEventListener("submit", handleFormSubmit);
    });
});
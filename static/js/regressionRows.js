let rowCount = 5;

function addRow() {
    const table = document.getElementById("inputTable");
    const row = table.insertRow(-1);
    row.classList.add("fade-in");

    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);

    cell1.innerHTML = `<div class="input-container"><input name="x${rowCount}" type="number" step="any" required placeholder=" "><label for="x${rowCount}">x${rowCount}</label></div>`;
    cell2.innerHTML = `<div class="input-container"><input name="y${rowCount}" type="number" step="any" required placeholder=" "><label for="y${rowCount}">y${rowCount}</label></div>`;

    console.log("Row added:", rowCount);
    rowCount++;
}

function removeRow() {
    const table = document.getElementById("inputTable");
    if (rowCount > 1) {
        const lastRow = table.rows[table.rows.length - 1];
        lastRow.classList.add("fade-out");

        setTimeout(() => {
            if (lastRow && lastRow.parentNode) {
                table.deleteRow(-1);
            }
        }, 300);

        rowCount--;
        console.log("Row removed:", rowCount);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const addBtn = document.getElementById("addRowBtn");
    const removeBtn = document.getElementById("removeRowBtn");

    if (addBtn) addBtn.addEventListener("click", addRow);
    if (removeBtn) removeBtn.addEventListener("click", removeRow);
});
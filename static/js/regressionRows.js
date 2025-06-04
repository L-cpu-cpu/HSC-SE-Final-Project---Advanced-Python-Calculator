let rowCount = 5;

function addRow() {
    const table = document.getElementById("inputTable");
    const row = table.insertRow(-1);

    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);

    cell1.innerHTML = `<input name="x${rowCount}" type="number" step="any" required />`;
    cell2.innerHTML = `<input name="y${rowCount}" type="number" step="any" required />`;

    console.log("Row added:", rowCount);
    rowCount++;
}

function removeRow() {
    const table = document.getElementById("inputTable");
    if (rowCount > 1) {
        table.deleteRow(-1);
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
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formulaSelect");

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            const selectedFormula = document.getElementById("specificFormula").value;
            const equation = formulaEquations[selectedFormula] || "";
            // Fallback warning if equation doesn't exist
            if (!equation) {
                // Optionally handle missing equation here
            }

            let existing = document.querySelector('input[name="equation"]');
            if (existing) {
                existing.value = equation;
            } else {
                const eqInput = document.createElement("input");
                eqInput.type = "hidden";
                eqInput.name = "equation";
                eqInput.value = equation;
                form.appendChild(eqInput);
            }

            form.submit();
        });
    }

    const categoryOptions = {
        areaAndPerim: [{text: 'Triangles', value: 'triangles'}, {text: 'Quadrilaterals', value: 'quadrilaterals'}, {text: 'Circles', value: 'circles'}],
        Trig: [{text: 'Pythagoras', value: 'pythagoras'}, {text: 'Rules', value: 'rules'}],
        poly: [{text: 'Quadratics', value: 'quadratics'}, {text: 'Cubics', value: 'cubics'}, {text: 'Quartics', value: 'quartics'}],
        phys: [{text: 'Newtonian', value: 'newtonian'}, {text: '...?', value: '...?'}, {text: '...? ', value: '...?'}]
    };
    const subOptions = {
    triangles: [{text: 'Right angle Triangles', value: 2}, {text: 'Non-right angle Triangles', value: 3}],
    quadrilaterals: [{text: 'Rectangles and Parallelograms', value: 2}, {text: 'Rhombuses and Kites', value: 2}],
    circles: [{text: 'Area', value: 1}, {text: 'Circumference', value: 1}, {text: 'Sector Area', value: 2}, {text: 'Arc Length', value: 2}],
    pythagoras: [{text: 'Hypotenuse', value: 2}, {text: 'Hypotenuse (Sine)', value: 2}, {text: 'Hypotenuse (Cosine)', value: 2}, {text: 'Opposite', value: 2}, {text: 'Adjacent', value: 2}, {text: 'Tangent (Opposite)', value: 2}, {text: 'Tangent (Adjacent)', value: 2}, {text: 'Angle (Tangent)', value: 2}],
    rules: [{text: 'Sine Rule (Angle)', value: 3}, {text: 'Sine Rule (Side)', value: 3}, {text: 'Cosine Rule (Angle)', value: 3}, {text: 'Cosine Rule (Side)', value: 3}],
    quadratics: [{text: 'Find y (quadratic)', value: 4}, {text: 'Quadratic Formula', value: 3}, {text: 'Vertex (x)', value: 2}, {text: 'Vertex (y)', value: 3}, {text: 'First derivative (quadratic)', value: 3}, {text: 'Second derivative (quadratic)', value: 2}],
    cubics: [{text: 'Find y (cubic)', value: 5}, {text: 'First derivative (cubic)', value: 4}, {text: 'Second derivative (cubic)', value: 3}, {text: 'Third derivative (cubic)', value: 2}],
    quartics: [{text: 'Find y (quartic)', value: 6}, {text: 'First derivative (quartic)', value: 5}, {text: 'Second derivative (quartic)', value: 4}, {text: 'Third derivative (quartic)', value: 3}, {text: 'Fourth derivative', value: 2}],
    newtonian: [{text: 'Second Law (Force)', value: 2}, {text: 'Second Law (Mass)', value: 2}, {text: 'Second Law (Acceleration)', value: 2}]
    };

    const InputPlaceholders = {
    triangles: {
        'Right angle Triangles': ['Base', 'Height'],
        'Non-right angle Triangles': ['Side A', 'Side B', 'Included Angle']
    },
    quadrilaterals: {
        'Rectangles and Parallelograms': ['Base', 'Height'],
        'Rhombuses and Kites': ['Diagonal 1', 'Diagonal 2']
    },
    circles: {
        'Area': ['Radius (r)'],
        'Circumference': ['Radius (r)'],
        'Sector Area': ['Radius (r)', 'Angle (θ)'],
        'Arc Length': ['Radius (r)', 'Angle (θ)']
    },
    pythagoras: {
        'Hypotenuse': ['Side A', 'Side B'],
        'Hypotenuse (Sine)': ['Opposite', 'Angle (θ)'],
        'Hypotenuse (Cosine)': ['Adjacent', 'Angle (θ)'],
        'Opposite': ['Hypotenuse', 'Angle (θ)'],
        'Adjacent': ['Hypotenuse', 'Angle (θ)'],
        'Tangent (Opposite)': ['Adjacent', 'Angle (θ)'],
        'Tangent (Adjacent)': ['Opposite', 'Angle (θ)'],
        'Angle (Tangent)': ['Opposite', 'Adjacent']
    },
    rules: {
        'Sine Rule (Angle)': ['Side A', 'Side B', 'Angle A'],
        'Sine Rule (Side)': ['Angle A', 'Angle B', 'Side A'],
        'Cosine Rule (Angle)': ['Side A', 'Side B', 'Opposite Side'],
        'Cosine Rule (Side)': ['Angle A', 'Angle B', 'Opposite Angle']
    },
    quadratics: {
        'Find y (quadratic)': ['a', 'b', 'c', 'x'],
        'Quadratic Formula': ['a', 'b', 'c'],
        'Vertex (x)': ['a', 'b'],
        'Vertex (y)': ['a', 'b', 'c'],
        'First derivative (quadratic)': ['a', 'b', 'x'],
        'Second derivative (quadratic)': ['a', 'x']
    },
    cubics: {
        'Find y (cubic)': ['a', 'b', 'c', 'd', 'x'],
        'First derivative (cubic)': ['a', 'b', 'c', 'x'],
        'Second derivative (cubic)': ['a', 'b', 'x'],
        'Third derivative (cubic)': ['a', 'x']
    },
    quartics: {
        'Find y (quartic)': ['a', 'b', 'c', 'd', 'e', 'x'],
        'First derivative (quartic)': ['a', 'b', 'c', 'd', 'x'],
        'Second derivative (quartic)': ['a', 'b', 'c', 'x'],
        'Third derivative (quartic)': ['a', 'b', 'x'],
        'Fourth derivative': ['a', 'x']
    },
    newtonian: {
        'Second Law (Force)': ['Mass (m)', 'Acceleration (a)'],
        'Second Law (Mass)': ['Force (F)', 'Acceleration (a)'],
        'Second Law (Acceleration)': ['Force (F)', 'Mass (m)']
    },
    };
        const formulaEquations = {
        "Right angle Triangles": "A = ½ × base × height",
        "Non-right angle Triangles": "Use sine rule",
        "Rectangles and Parallelograms": "A = base × height",
        "Rhombuses and Kites": "A = ½ × d₁ × d₂",
        "Area": "A = πr²",
        "Circumference": "C = 2πr",
        "Sector Area": "A = (θ/360) × πr²",
        "Arc Length": "L = (θ/360) × 2πr",
        "Hypotenuse": "c² = a² + b²",
        "Hypotenuse (Sine)": "h = o / sin(θ)",
        "Hypotenuse (Cosine)": "h = a / cos(θ)",
        "Opposite": "o = h × sin(θ)",
        "Adjacent": "a = h × cos(θ)",
        "Tangent (Opposite)": "o = a × tan(θ)",
        "Tangent (Adjacent)": "a = o / tan(θ)",
        "Angle (Tangent)": "θ = tan⁻¹(o / a)",
        "Sine Rule (Angle)": "sin A / a = sin B / b",
        "Sine Rule (Side)": "a / sin A = b / sin B",
        "Cosine Rule (Angle)": "cos C = (a² + b² - c²) / 2ab",
        "Cosine Rule (Side)": "c² = a² + b² - 2ab cos C",
        "Find y (quadratic)": "y = ax² + bx + c",
        "Quadratic Formula": "x = [-b ± √(b² - 4ac)] / 2a",
        "Vertex (x)": "x = -b / 2a",
        "Vertex (y)": "y = c - (b² / 4a)",
        "First derivative (quadratic)": "dy/dx = 2ax + b",
        "Second derivative (quadratic)": "d²y/dx² = 2a",
        "Find y (cubic)": "y = ax³ + bx² + cx + d",
        "First derivative (cubic)": "dy/dx = 3ax² + 2bx + c",
        "Second derivative (cubic)": "d²y/dx² = 6ax + 2b",
        "Third derivative (cubic)": "d³y/dx³ = 6a",
        "Find y (quartic)": "y = ax⁴ + bx³ + cx² + dx + e",
        "First derivative (quartic)": "dy/dx = 4ax³ + 3bx² + 2cx + d",
        "Second derivative (quartic)": "d²y/dx² = 12ax² + 6bx + 2c",
        "Third derivative (quartic)": "d³y/dx³ = 24ax + 6b",
        "Fourth derivative": "d⁴y/dx⁴ = 24a",
        "Second Law (Force)": "F = m × a",
        "Second Law (Mass)": "m = F / a",
        "Second Law (Acceleration)": "a = F / m"
    };

    const radios = document.querySelectorAll('input[name="category"]');
    const itemsSelect = document.getElementById('formula');

    if (!radios.length || !itemsSelect) {
        console.warn("Elements not found!");
        return;
    }

    radios.forEach(radio => {
        radio.addEventListener('change', function () {
            const selectedCategory = this.value;
            const items = categoryOptions[selectedCategory] || [];

            // Reset the first dropdown
            itemsSelect.innerHTML = '<option value="">Please choose a subcategory</option>';

            // Reset the second dropdown
            const subFormulaSelect = document.getElementById('specificFormula');
            subFormulaSelect.innerHTML = '<option value="">Choose a formula</option>';

            // Clear any existing inputs
            const inputContainer = document.getElementById('dynamicInputs');
            inputContainer.innerHTML = '';

            // Populate first dropdown
            items.forEach(item => {
                const option = document.createElement('option');
                option.value = item.value;
                option.textContent = item.text;
                itemsSelect.appendChild(option);
            });
        });
    });
    itemsSelect.addEventListener('change', function () {
        const selectedItem = this.value;
        const subFormulaSelect = document.getElementById('specificFormula');

        subFormulaSelect.innerHTML = '<option value="">Choose a formula</option>';

        const subs = subOptions[selectedItem] || [];
        subs.forEach(sub => {
            const option = document.createElement('option');
            option.value = sub.text;
            option.textContent = sub.text;
            subFormulaSelect.appendChild(option);
        });
        subFormulaSelect.addEventListener('change', function () {
            const inputContainer = document.getElementById('dynamicInputs');
            inputContainer.innerHTML = ''; // Clear any previous inputs

            const selectedOption = this.options[this.selectedIndex];
            const selectedCategory = itemsSelect.value;
            const subItems = subOptions[selectedCategory] || [];
            const matchingItem = subItems.find(item => item.text === selectedOption.text);
            const numInputs = matchingItem ? matchingItem.value : 0;

            const selectedText = selectedOption.text;
            const categoryPlaceholders = InputPlaceholders[selectedCategory] || {};
            const placeholders = categoryPlaceholders[selectedText] || [];

            for (let i = 0; i < numInputs; i++) {
                const input = document.createElement('input');
                input.type = 'text';
                input.name = "dynamicInput";
                input.placeholder = placeholders[i] || `Input ${i + 1}`;
                inputContainer.appendChild(input);
                inputContainer.appendChild(document.createElement('br'));
            }
        });
    });
});
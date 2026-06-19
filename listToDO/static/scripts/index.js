// 1. Select your DOM elements and base URL ONCE
const table_row = document.getElementById("tbody");
const current_url = window.location.origin;

// 2. Fetch and render your tasks
fetch(`${current_url}/all-tasks`)
    .then((dataa) => dataa.json())
    .then((tasks) => {
        // Clear the table once before rendering the new list
        table_row.innerHTML = "";

        // Loop through and APPEND each row safely
        tasks.forEach((task) => {
            table_row.innerHTML += `<tr scope="row"><td>${task.task_content}</td></tr>`;
        });
    })
    .catch((err) => console.error("Error loading tasks:", err));

table_row.addEventListener("click", (e) => {
    const tar = e.target;
    if (tar.tagName === "TD") {
        if (tar.style.textDecoration === "line-through") {
            tar.style.textDecoration = "none";
            tar.style.color = "black";
        } else {
            tar.style.textDecoration = "line-through";
            tar.style.color = "gray";
        }
    }
});

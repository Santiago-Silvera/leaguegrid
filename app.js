const fetchQuestions = async () => {
    try {
        // Construct the request URL with the row and col
        const response = await fetch(`/get_question`);
        if (response.ok) {
            const data = await response.json();
            console.log("Data from fetchQuestions: " + data);
            return data.questions; // Assuming the server returns a 'text' field
        } else {
            console.error(`Failed to fetch questions`);
            return {};
        }
    } catch (error) {
        console.error("Error fetching cell data:", error);
        return {};
    }
};
const fillGrid = async () => {
    const gridContainer = document.getElementById("grid");
    const gridSize = 3; // 3 (champs) + 1 (question)
    for (let row = 0; row < gridSize; row++) {
        for (let col = 0; col < gridSize; col++) {
            let div = document.createElement("div");
            div.className = "bg-gray-700 w-32 h-32 transition-colors duration-200 hover:bg-gray-500";

            gridContainer.appendChild(div);
        }
    }
};

document.addEventListener("DOMContentLoaded", fillGrid);

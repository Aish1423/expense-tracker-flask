const ctx = document.getElementById('expenseChart');

if (ctx) {

    new Chart(ctx, {

        type: 'doughnut',

        data: {

            labels: ['Income', 'Expense'],

            datasets: [{

                data: [5000, 2000],

                backgroundColor: [
                    '#22c55e',
                    '#ef4444'
                ]

            }]

        }

    });

}
function toggleDarkMode() {

    document.body.classList.toggle("bg-white");
    document.body.classList.toggle("text-black");

}

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", () => {

        console.log(searchInput.value);

    });

}
function showToast(message) {

    const toast = document.createElement("div");

    toast.innerText = message;

    toast.className = `
        fixed top-5 right-5
        bg-green-500
        text-white
        px-6 py-4
        rounded-xl
        shadow-2xl
    `;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3000);

} 

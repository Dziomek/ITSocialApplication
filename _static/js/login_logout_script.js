$(function () {
    $('[data-bs-toggle="popover"]').popover()
})

function addYears() {
    const yearSelect = document.getElementsByName("Year")[0]
    for (let i=1900; i<=2022; i++) {
        const option = document.createElement('option')
        option.value = String(i)
        option.innerText = String(i)
        yearSelect.appendChild(option)
    }
}

function addMonths() {
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const monthsSelect = document.getElementsByName("Month")[0]
    
    for (const month of months) {
        const option = document.createElement('option')
        option.value = month
        option.innerText = month
        monthsSelect.appendChild(option)
    }
}

function addDays() {
    let daysToCreate
    const daySelect = document.getElementsByName("Day")[0]
    daySelect.value = "1"
    const monthsSelect = document.getElementsByName("Month")[0]
    const selectedMonth = monthsSelect.selectedOptions[0].value
    console.log(selectedMonth)
    const first_group = ["January", "March", "May", "July", "August", "October", "December"]
    const second_group = ["April", "June", "September", "November"]

    if (first_group.includes(selectedMonth)) {
        daysToCreate = 31
    }
    else if (second_group.includes(selectedMonth)) {
        daysToCreate = 30
    }
    else {
        const yearSelect = document.getElementsByName("Year")[0]
        const selectedYear = yearSelect.selectedOptions[0].value
        if (Number(selectedYear) % 4 === 0) {
            daysToCreate = 29
        }
        else {
            daysToCreate = 28

        }
    }
    for(let i=1; i<=daysToCreate; i++) {
        const option = document.createElement('option')
        option.value = String(i)
        option.innerText = String(i)
        daySelect.appendChild(option)
    }

}

addYears()
addMonths()
addDays()
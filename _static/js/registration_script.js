function checkSubmit() {

    const formFields = document.getElementsByClassName('form-control')
    console.log(formFields.length)
    for (const field of formFields) {
        console.log(field.value)
        if (!field.value) {
            console.log('PUSTE POLE')

            return false
        }
    }

    return formFields[2].value === formFields[3].value
}
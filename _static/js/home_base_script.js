function active() {
    const buttons = document.getElementsByClassName('navigation')
    for (const button of buttons) {
        button.addEventListener('click', e => {
            current = document.getElementsByClassName('nav__btn-active')[0]
            current.classList.remove('nav__btn-active')
            parent = e.target.parentElement
            parent.classList.add('nav__btn-active')
        })
    }
}

active()
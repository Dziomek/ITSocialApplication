function setHome() {
    const homeButton = document.getElementById("homeButton")
    const forumButton = document.getElementById("forumButton")
    const messagesButton = document.getElementById("messagesButton")
    const parentElement = homeButton.parentElement.parentElement
    const forumParent = forumButton.parentElement.parentElement
    const messagesElement = messagesButton.parentElement.parentElement
    forumParent.classList.remove('nav__btn-active')
    messagesElement.classList.remove('nav__btn-active')
    parentElement.classList.add('nav__btn-active')
}

setHome()

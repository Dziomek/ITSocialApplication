function setHome() {
    const homeButton = document.getElementById("homeButton")
    const forumButton = document.getElementById("forumButton")
    const parentElement = homeButton.parentElement.parentElement
    const forumParent = forumButton.parentElement.parentElement
    forumParent.classList.remove('nav__btn-active')
    parentElement.classList.add('nav__btn-active')

}

setHome()

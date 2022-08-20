function setForum() {
    const homeButton = document.getElementById("homeButton")
    const forumButton = document.getElementById("forumButton")
    const parentElement = forumButton.parentElement.parentElement
    const homeParent = homeButton.parentElement.parentElement
    homeParent.classList.remove('nav__btn-active')
    parentElement.classList.add('nav__btn-active')
    parentElement.style = 'border-bottom: 3px solid gray'
    homeParent.style.border = 'none'
}


setForum()
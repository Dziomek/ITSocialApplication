function setPost() {
    const homeButton = document.getElementById("homeButton")
    const forumButton = document.getElementById("forumButton")
    const forumParent = forumButton.parentElement.parentElement
    const homeParent = homeButton.parentElement.parentElement
    homeParent.classList.remove('nav__btn-active')
    forumParent.classList.remove('nav__btn-active')
    homeParent.style.border = 'none'
    forumParent.style.border = 'none'
}

setPost()
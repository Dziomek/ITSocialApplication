function setMessages() {
    const homeButton = document.getElementById("homeButton")
    const forumButton = document.getElementById("forumButton")
    const messagesButton = document.getElementById("messagesButton")
    const parentElement = forumButton.parentElement.parentElement
    const homeParent = homeButton.parentElement.parentElement
    const messagesElement = messagesButton.parentElement.parentElement
    homeParent.classList.remove('nav__btn-active')
    messagesElement.classList.add('nav__btn-active')
    parentElement.classList.remove('nav__btn-active')
    messagesElement.style = 'border-bottom: 3px solid gray'
    homeParent.style.border = 'none'
    parentElement.style.border = 'none'
    console.log('nastawione')
}

setMessages()
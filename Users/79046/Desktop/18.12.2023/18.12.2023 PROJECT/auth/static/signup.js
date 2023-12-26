function checkPasswords() {
    const isValid = password.checkValidity()
    const isEqual = password.value === passwordConfirm.value

    // console.log(passwordConfirm.value);
    // if (password.textContent != passwordConfirm.textContent){
    if (!isValid || !isEqual){
        passwordConfirm.setCustomValidity("Passwords don't match");
        button.setAttribute("disabled", "disabled");
    } else {
        console.log("!");
        passwordConfirm.setCustomValidity("");
        button.removeAttribute("disabled");
    }
}

const [password, passwordConfirm] = document.querySelectorAll(input[type = "password"]);
const button = document.querySelector('form button');


Array.of(password, passwordConfirm).forEach(el => {
    el.addEventListener('input', checkPasswords)
})

console.log(password, passwordConfirm)

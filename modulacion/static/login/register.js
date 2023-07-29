const nombre = document.getElementById("name")
const curp = document.getElementById("curp")
const email = document.getElementById("email")
const tuition = document.getElementById("tuition")
const pass1 = document.getElementById("pass1")
const pass2 = document.getElementById("pass2")
const form = document.getElementById("form")
const war = document.getElementById("warnings")

form.addEventListener("submit", e =>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regerxEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    if(regerxEmail.test(email.value)){
        warnings += `El correo electronico no es valido <br>`
        entrar = true
    }
    if(curp.value.length != 18){
        warnings += `La CURP no es valida <br>`
        entrar = true
    }
    if(pass1.value.length < 8){
        warnings += `La contraseña es muy corta <br>`
        entrar = true
    }
    if(pass1 != pass2){
        warnings += `Las contraseñas no coinciden <br>`
        entrar = true
    }
    if(entrar){
        war.innerHTML = warnings
    }
})
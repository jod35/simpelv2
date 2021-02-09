const signUpLink=document.querySelector('.sign-up');
const loginLink=document.querySelector('.login');
const signUpModal=document.querySelector('.signup-form-modal');
const loginModal=document.querySelector('.login-form-modal');

signUpLink.addEventListener('click',()=>{
        signUpModal.style.display="block"
})

loginLink.addEventListener('click',()=>{
    loginModal.style.display="block"
})


const closeModal=(id)=>{
    let el = document.getElementById(id);

    el.style.display="none"
}
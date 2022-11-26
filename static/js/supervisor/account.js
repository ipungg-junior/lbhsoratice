/* Sidebar - Side navigation menu on mobile/responsive mode */
function toggleNavbar(collapseID) {
    document.getElementById(collapseID).classList.toggle("hidden");
    document.getElementById(collapseID).classList.toggle("bg-white");
    document.getElementById(collapseID).classList.toggle("m-2");
    document.getElementById(collapseID).classList.toggle("py-3");
    document.getElementById(collapseID).classList.toggle("px-6");
}
/* Function for dropdowns */
function openDropdown(event, dropdownID) {
    let element = event.target;
    while (element.nodeName !== "A") {
        element = element.parentNode;
    }
    var popper = Popper.createPopper(element, document.getElementById(dropdownID), {
        placement: "bottom-end"
    });
    document.getElementById(dropdownID).classList.toggle("hidden");
    document.getElementById(dropdownID).classList.toggle("block");
}

function checkPassword(pas, confPas) {
    if (pas == confPas) {
        return true
    } else {
        return false
    }
}

function checkAllField(fullname, email, password, confPassword){
    if(fullname==""){
        return false
    }
    if(email==""){
        return false
    }
    if(password==""){
        return false
    }
    if(confPassword==""){
        return false
    }
    else{
        return true
    }
}

var modal = document.getElementById('modal-buat-akun');
var btnModal = document.getElementById('button-buat-akun');
var btnDaftar = document.getElementById('button-daftar-akun');
var exit = document.getElementById('button-exit');

btnModal.addEventListener('click', function () {
    modal.style.display = 'flex';
})
exit.addEventListener('click', function () {
    modal.style.display = 'none';
})

btnDaftar.addEventListener('click', function () {
    var preLoader = document.getElementById('pre-loader');
    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var fullname = document.getElementById('input-nama-lengkap').value;
    var mail = document.getElementById('input-email').value;
    var password = document.getElementById('input-password').value;
    var confPassword = document.getElementById('input-konfirmasi-password').value;

    // POST DATA REGISTER ACCOUNT
    async function post() {
        preLoader.style.display = 'flex';
        const setting = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            },
            body: JSON.stringify({
                'fullname': fullname,
                'email': mail,
                'password': password,
                'confirmation_password': confPassword
            })
        }

        let response = await fetch('/supervisor/accounts/register/', setting);

        if (response.status === 200) {

            preLoader.style.display = 'none';
            modal.style.display = 'none';
        } else {

            preLoader.style.display = 'none';
            modal.style.display = 'none';
        }
    }
    if (checkAllField(fullname, mail, password, confPassword)) {
        if (checkPassword(password, confPassword)) {
            post();
            document.getElementById('input-nama-lengkap').value = "";
            document.getElementById('input-email').value = "";
            document.getElementById('input-password').value = "";
            document.getElementById('input-konfirmasi-password').value = "";
        } else {
            document.getElementById('input-password').value = "";
            document.getElementById('input-konfirmasi-password').value = "";
        }
    }
    else{
        console.log("Field null");
    }


})


function deleteArticle(accountID) {
    var result = confirm("Akun akan dihapus secara permanen, yakin?");
    if (result) {
        // Delete article by POST API
        console.log('Remove function delete article -> ' + slug);
    }
}
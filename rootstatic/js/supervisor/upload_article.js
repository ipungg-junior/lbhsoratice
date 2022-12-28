var tag = [];

var modal = document.getElementById('modal-buat-tag');
var btnModal = document.getElementById('show-buat-tag');
var btnDaftar = document.getElementById('button-buat-tag');
var exit = document.getElementById('button-exit');
var menu = document.getElementById('tag-list-menu');

btnModal.addEventListener('click', function () {
    modal.style.display = 'flex';
    menu.classList.add('hidden');
})
exit.addEventListener('click', function () {
    modal.style.display = 'none';
})

btnDaftar.addEventListener('click', function () {
    alert('Javascript error! (NO CODE)');
})

function openTagList(){
    
    if (menu.classList.contains('hidden')){
        menu.classList.remove('hidden');
    }else{
        menu.classList.add('hidden');
    }
}

function selectTag(nametag){
    if (!(tag.includes(nametag))){
        tag.push(nametag);
        var ul = document.getElementById("tag-selected-list");
        var li = document.createElement("li");
        var a = document.createElement("a");
        var i = document.createElement("i");
        a.appendChild(document.createTextNode(nametag));
        li.setAttribute('class', 'px-2');
        i.setAttribute('class', 'mx-1 fas fa-window-close cursor-pointer');
        i.setAttribute('onclick', "removeTag('"+nametag+"')");
        li.setAttribute('id', nametag);
        li.appendChild(a);
        li.appendChild(i);
        ul.appendChild(li);
    }
}


function removeTag(nametag){
    if (tag.includes(nametag)){
        tag.forEach(function ( elem, index ) {
            if (elem==nametag){
                document.getElementById(elem).remove();
                tag.splice(index, 1);
            }
        });

    }
        //var ul = document.getElementById("tag-selected-list");
        //var li = document.createElement("li");
}



async function deleteTagFromDB(nametag){
    var ret = confirm("Anda yakin akan menghapus tag \"" + nametag + "\" ?");
    if (ret){
        let response = await fetch('/supervisor/delete-tag/'+nametag+"/");
        if (response.status===200){
            window.href.location = "/supervisor/upload-article/";
        }else{
            alert("Gagal menghapus tag.");
        }
    }else{
        alert("membatalkan haus tag.");
    }
}

// Image upload handler
let img = document.getElementById('image-upload');
let icon = document.getElementById('icon-download');
let captionIcon = document.getElementById('caption-download');
img.onchange = uploadHandler;
function uploadHandler() {
    const [file] = img.files;
    if (file) {
        document.getElementById('file-image').src = URL.createObjectURL(file);
        document.getElementById('file-image').onload = function () {
            URL.revokeObjectURL(document.getElementById('file-image').src) // free memory
            icon.style.display = "none";
            captionIcon.style.display = "none";
        }
    }
}

// Title Input
const inpTitle = document.getElementById('input-title');
inpTitle.onclick = changeBold;
function changeBold() {
    inpTitle.style.fontWeight = 500;
}


/**
 * Summernote content 
 */

var quill = new Quill('#editor', {
    theme: 'snow',
});
const btnPosting = document.getElementById('button-posting');
btnPosting.onclick = uploadArticle;
let base64file = '';
var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

function uploadArticle() {
    //ambil data gambar
    var unImg = document.getElementById('image-upload');
    let file = unImg.files[0];
    let reader = new FileReader();
    //ambil title
    var title = document.getElementById('input-title').value;
    //ambil data content summernote    
    var summernoteContent = quill.root.innerHTML;

    reader.onloadend = function () {
        if (file == null) {
            console.log("No image");
        }else{
        base64file = reader.result;

        async function postArticle() {
            const setting = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
                body: JSON.stringify({
                    'title': title,
                    'content': summernoteContent,
                    'img': base64file,
                    'tag': tag
                })
            }

            let response = await fetch('/supervisor/upload-article/', setting);

            if (response.status === 200) {
                window.location.href = '/supervisor/';
            }
            URL.revokeObjectURL(file);
            unImg.value = null;
        }
            postArticle();
        }
    }
    if (summernoteContent == "<p><br></p>" || title =="") {
        alert("Harap isi konten artikel");
    } else {
        //send article
        try {
            reader.readAsDataURL(file);
        }
        catch (e) {
            alert("Harap upload gambar!");
        }
    }
}


function deleteArticle(slug) {
    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var result = confirm("Want to delete?");
    if (result) {
        console.log(csrf_token);
        async function deleteArticle() {
            const setting = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
                body: JSON.stringify({})
            }

            let response = await fetch(('/supervisor/delete/'+slug+'/'), setting);

            if (response.status === 200) {
                window.location.href = '/supervisor/';
            }else{
                alert("Gagal menghapus, coba lagi . . .");
            }
        }
        deleteArticle();
    }
}
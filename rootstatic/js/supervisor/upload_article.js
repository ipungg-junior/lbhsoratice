
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
    var summernoteFrame = document.getElementById('id_content_iframe').contentWindow.document.body.firstElementChild;
    var summernoteContent = summernoteFrame.nextElementSibling.getElementsByClassName('note-editable')[0].innerHTML;
    reader.onloadend = function () {
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
                })
            }

            let response = await fetch('/supervisor/upload-article/', setting);

            if (response.status === 200) {
                console.log('success');
            }
        }
        postArticle();
    }
    //send article
    reader.readAsDataURL(file);
}


function deleteArticle(slug) {
    var result = confirm("Want to delete?");
    if (result) {
        // Delete article by POST API
        console.log('Remove function delete article -> ' + slug);
    }
}
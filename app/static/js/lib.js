function file_selected(element){
    var path = element.value;
    var errorMsg;
    if(!path.endWith('jpg') && !path.endWith('gif'
        && !path.endWith('png'))){
        errorMsg = 'Only PNG, GIF, or JPG pictures are supported.';
    }
    //load this file in a modal dialog
    var imgDragArea = `<div class="modal fade" ></div>`
}

function save_avatar(){
    
}
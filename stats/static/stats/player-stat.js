function expandConstract(box) {
    var boxButton = box.querySelector('i');
    var cardBody = box.parentElement.parentElement.parentElement.querySelector('.panel-body');
    if(boxButton.classList.contains('bi-arrows-angle-expand')) {
        boxButton.classList.replace('bi-arrows-angle-expand', 'bi-arrows-angle-contract');
        cardBody.classList.replace('panel-close', 'panel-open');
    }
    else {
        boxButton.classList.replace('bi-arrows-angle-contract', 'bi-arrows-angle-expand');
        cardBody.classList.replace('panel-open', 'panel-close');
    }
}
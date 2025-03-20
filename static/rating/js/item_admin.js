function createRatingItem() {
    const createItemUrl = $('#create_item_url').val();
    generateAutoReloadWindow(createItemUrl + '?type=create', 'height=600, width=600, top=0,left=0,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
}

function deleteSelectRatingItem() {
    $('#delete_form').submit();
}

function clickRatingItem(item_id) {
    // const itemDetailUrl = $('#item_detail_url').val();
    // window.location.href = itemDetailUrl + '?item_id=' + item_id.toString();
}
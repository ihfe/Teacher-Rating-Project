$('#select_all_checkbox').click(function () {
    if ($(this).is(':checked')) {
        $(".choose_box").each(function () {
            $(this).prop("checked", true);
        });
    } else {
        $(".choose_box").each(function () {
            $(this).prop("checked", false);
        });
    }
});

function deleteSelectEvent() {
    $('#delete_form').submit();
}

function createRatingEvent() {
    const createEventUrl = $('#create_event_url').val();
    window.location.href = createEventUrl;
}

function clickEventDetail(event_id) {
    const eventDetailUrl = $('#event_detail_url').val();
    window.location.href = eventDetailUrl + '?event_id=' + event_id.toString();
}
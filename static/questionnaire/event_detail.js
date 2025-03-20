/**
 * 问卷提交处理函数
 * 防止重复提交表单
 */
function disableSubmitButton() {
    $('#submit_button').prop('disabled', true);
}
// Panel模块公共函数

/**
 * 删除选中的项目
 * @param {string} formId - 表单ID
 */
function deleteSelected(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.submit();
    }
}

/**
 * 创建课程
 */
function createLesson() {
    generateAutoReloadWindow('/panel/create_lesson?type=create', 'height=600, width=600, top=0,left=0,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
}

/**
 * 点击更新课程
 * @param {string} lessonId - 课程ID
 */
function clickUpdateLesson(lessonId) {
    generateAutoReloadWindow('/panel/create_lesson?type=update&lesson_id=' + lessonId, 'height=600, width=600, top=0,left=0,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
}

/**
 * 生成自动刷新的弹出窗口
 * @param {string} url - 窗口URL
 * @param {string} windowFeatures - 窗口特性
 */
function generateAutoReloadWindow(url, windowFeatures) {
    const popup = window.open(url, '_blank', windowFeatures);
    if (popup) {
        popup.onbeforeunload = function() {
            setTimeout(function() {
                window.location.reload();
            }, 500);
        };
    }
}

/**
 * 全选/取消全选复选框
 * @param {string} selectAllId - 全选复选框ID
 * @param {string} itemClass - 选项复选框类名
 */
function toggleSelectAll(selectAllId, itemClass) {
    const selectAllCheckbox = document.getElementById(selectAllId);
    const itemCheckboxes = document.getElementsByClassName(itemClass);
    
    selectAllCheckbox.addEventListener('click', function() {
        Array.from(itemCheckboxes).forEach(checkbox => {
            checkbox.checked = selectAllCheckbox.checked;
        });
    });
}

/**
 * 删除选中项
 * @param {string} formId - 表单ID
 */
function deleteSelected(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.submit();
    }
}

/**
 * 创建课程
 */
function createLesson() {
    generateAutoReloadWindow('/panel/create_lesson?type=create', 'height=600, width=600, top=0,left=0,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
}

/**
 * 点击更新课程
 * @param {string} lessonId - 课程ID
 */
function clickUpdateLesson(lessonId) {
    generateAutoReloadWindow('/panel/create_lesson?type=update&lesson_id=' + lessonId, 'height=600, width=600, top=0,left=0,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
}
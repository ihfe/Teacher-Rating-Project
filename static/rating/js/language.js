// rating模块的语言配置
const ratingLanguage = {
    'zh-CN': {
        'teacherDetailStats': '教师详细统计',
        'classDetailStats': '班级详细统计',
        'courseTeacher': '任课教师',
        'class': '班级',
        'course': '课程',
        'totalScore': '总分',
        'description': '描述',
        'teacherName': '教师姓名'
    },
    'en-US': {
        'teacherDetailStats': 'Teacher Detail Statistics',
        'classDetailStats': 'Class Detail Statistics',
        'courseTeacher': 'Course Teacher',
        'class': 'Class',
        'course': 'Course',
        'totalScore': 'Total Score',
        'description': 'Description',
        "teacherName": "Teacher Name"
    }
};

// 导出语言配置
Object.assign(window.languageData || {}, ratingLanguage);
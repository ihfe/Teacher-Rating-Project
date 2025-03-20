from django.test import TestCase, Client
from django.urls import reverse
from .models import TheClass, Lesson, Teacher, LessonOnClass, TeacherOnLessonOnClass

class PanelTests(TestCase):
    def setUp(self):
        self.client = Client()
        # 创建测试数据
        self.test_class = TheClass.create(
            title='测试班级',
            head_teacher='测试班主任',
            description='用于测试的班级'
        )
        self.test_lesson = Lesson.create(
            title='测试课程',
            description='用于测试的课程'
        )
        self.test_teacher = Teacher.create(
            name='测试教师',
            description='用于测试的教师'
        )
        self.test_lesson_on_class = LessonOnClass.create(
            class_id=self.test_class.class_id,
            lesson_id=self.test_lesson.lesson_id
        )
        self.test_teacher_on_lesson = TeacherOnLessonOnClass.create(
            teacher_id=self.test_teacher.teacher_id,
            lc_id=self.test_lesson_on_class.lc_id
        )

    def test_class_list(self):
        """Test the class list page"""
        response = self.client.get(reverse('panel:class_admin'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page if not logged in

    def test_create_class(self):
        """Test create class"""
        response = self.client.get(reverse('panel:create_class'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page if not logged in

    def test_lesson_list(self):
        """Test the course list page"""
        response = self.client.get(reverse('panel:lesson_admin'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page if not logged in

    def test_teacher_list(self):
        """Test the teacher list page"""
        response = self.client.get(reverse('panel:teacher_admin'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page if not logged in

    def test_model_relationships(self):
        """Test the model relationships"""
        # 测试班级-课程关系
        lesson_on_class = LessonOnClass.select().where(
            LessonOnClass.class_id == self.test_class.class_id,
            LessonOnClass.lesson_id == self.test_lesson.lesson_id
        ).first()
        self.assertIsNotNone(lesson_on_class)

        # 测试教师-课程关系
        teacher_on_lesson = TeacherOnLessonOnClass.select().where(
            TeacherOnLessonOnClass.teacher_id == self.test_teacher.teacher_id,
            TeacherOnLessonOnClass.lc_id == self.test_lesson_on_class.lc_id
        ).first()
        self.assertIsNotNone(teacher_on_lesson)

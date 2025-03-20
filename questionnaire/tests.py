from django.test import TestCase, Client
from django.urls import reverse
from .models import AnswerSheet, AnswerItem
from rating.models import RatingEvent, LogRatingItem, LogRatingLevel, LogTeacherOnLessonOnClass

class QuestionnaireTests(TestCase):
    def setUp(self):
        self.client = Client()
        # 创建测试数据
        self.test_event = RatingEvent.create(
            title='测试评分事件',
            status=0,
            vote_type=0,
            classification=0,
            description='用于测试的评分事件'
        )
        self.test_log_item = LogRatingItem.create(
            event_id=self.test_event.event_id,
            title='测试评分项',
            description='用于测试的评分项'
        )
        self.test_log_level = LogRatingLevel.create(
            item_id=self.test_log_item.item_id,
            title='优秀',
            score=10
        )
        self.test_log_tlc = LogTeacherOnLessonOnClass.create(
            event_id=self.test_event.event_id,
            teacher_id=1,
            lc_id=1
        )

    def test_event_list(self):
        """测试问卷列表页面"""
        response = self.client.get(reverse('questionnaire:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/index.html')

    def test_event_overview(self):
        """测试问卷概览页面"""
        response = self.client.get(reverse('questionnaire:event_overview', args=[self.test_event.event_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/event_overview.html')

    def test_event_detail(self):
        """测试问卷详情页面"""
        response = self.client.get(reverse('questionnaire:event_detail', 
            args=[self.test_event.event_id, 0, 1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/event_detail.html')

    def test_submit_answer(self):
        """测试提交问卷答案"""
        data = {
            f'radio_{self.test_log_tlc.tlc_id}_{self.test_log_item.item_id}': self.test_log_level.level_id
        }
        response = self.client.post(reverse('questionnaire:event_detail',
            args=[self.test_event.event_id, 0, 1]), data)
        self.assertEqual(response.status_code, 302)  # 提交成功后重定向

        # 验证答案是否保存成功
        answer_sheet = AnswerSheet.select().where(
            AnswerSheet.event_id == self.test_event.event_id
        ).first()
        self.assertIsNotNone(answer_sheet)

        answer_item = AnswerItem.select().where(
            AnswerItem.answer_id == answer_sheet.answer_id,
            AnswerItem.tlc_id == self.test_log_tlc.tlc_id,
            AnswerItem.log_item_id == self.test_log_item.item_id,
            AnswerItem.log_level_id == self.test_log_level.level_id
        ).first()
        self.assertIsNotNone(answer_item)

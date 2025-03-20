from django.test import TestCase, Client
from django.urls import reverse
from .models import RatingEvent, RatingItem, RatingLevel, LogRatingItem, LogRatingLevel

class RatingTests(TestCase):
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
        self.test_item = RatingItem.create(
            title='测试评分项',
            description='用于测试的评分项'
        )
        self.test_level = RatingLevel.create(
            item_id=self.test_item.item_id,
            title='优秀',
            score=10
        )

    def test_event_list(self):
        """测试评分事件列表页面"""
        response = self.client.get(reverse('rating:event_admin'))
        self.assertEqual(response.status_code, 302)  # 未登录时重定向到登录页面

    def test_item_list(self):
        """测试评分项列表页面"""
        response = self.client.get(reverse('rating:item_admin'))
        self.assertEqual(response.status_code, 302)  # 未登录时重定向到登录页面

    def test_create_event(self):
        """测试创建评分事件"""
        response = self.client.get(reverse('rating:create_event'))
        self.assertEqual(response.status_code, 302)  # 未登录时重定向到登录页面

    def test_event_detail(self):
        """测试评分事件详情页面"""
        response = self.client.get(reverse('rating:event_detail', args=[self.test_event.event_id]))
        self.assertEqual(response.status_code, 302)  # 未登录时重定向到登录页面

    def test_model_relationships(self):
        """测试模型关系"""
        # 测试评分项-评分级别关系
        rating_level = RatingLevel.select().where(
            RatingLevel.item_id == self.test_item.item_id
        ).first()
        self.assertIsNotNone(rating_level)

        # 测试评分事件-评分项日志关系
        log_rating_item = LogRatingItem.create(
            event_id=self.test_event.event_id,
            title=self.test_item.title,
            description=self.test_item.description
        )
        log_rating_level = LogRatingLevel.create(
            item_id=log_rating_item.item_id,
            title=self.test_level.title,
            score=self.test_level.score
        )
        self.assertIsNotNone(log_rating_item)
        self.assertIsNotNone(log_rating_level)

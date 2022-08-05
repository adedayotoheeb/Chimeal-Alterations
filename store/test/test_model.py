from django.test import TestCase
from store.models import Product, Order, Category, Post, Comment


class TestPostModel(TestCase):

    def setUp(self) -> None:
        self.data_entry = Comment.objects.create(
            name="Chimeal", email="Chimeal@gmail.com", message="i love cloth")

    def test_comment_model(self):
        """
        Testing Post model data insertion
        """
        data = self.data_entry
        self.assertTrue(isinstance(data, Comment))
        self.assertEqual(data.name, 'Chimeal')
        self.assertEqual(data.email, 'Chimeal@gmail.com')
        self.assertEqual(data.message, "i love cloth")
        self.assertEqual(str(data), "Chimeal")

class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.data_entry = Category.objects.create(
            name="Chimeal", slug='chimeal')

    def test_category_model(self) -> None:
        """
        Testing Category model insertion
        """
        data = self.data_entry
        self.assertEqual(data.name,"Chimeal")
        self.assertEqual(data.slug,"chimeal")
        self.assertEqual(str(data), "Chimeal")
        self.assertTrue(isinstance(data, Category))

class TestProductModel(TestCase):
    pass
        

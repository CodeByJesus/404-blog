from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Category, Tag

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura datos que se usarán en todas las pruebas de esta clase
        User = get_user_model()
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.category = Category.objects.create(name='Test Category', slug='test-category')
        cls.tag1 = Tag.objects.create(name='Test Tag 1', slug='test-tag-1')
        cls.tag2 = Tag.objects.create(name='Test Tag 2', slug='test-tag-2')

    def test_post_creation(self):
        # Prueba que un post se puede crear correctamente
        post = Post.objects.create(
            titulo='Mi Primer Post de Prueba',
            contenido='Contenido de prueba para el post.',
            autor=self.user,
            category=self.category,
            is_pinned=False
        )
        post.tags.add(self.tag1, self.tag2) # Añadir tags

        self.assertEqual(post.titulo, 'Mi Primer Post de Prueba')
        self.assertEqual(post.autor, self.user)
        self.assertEqual(post.category, self.category)
        self.assertTrue(post.tags.count() == 2) # Verificar que se añadieron 2 tags
        self.assertIn(self.tag1, post.tags.all())
        self.assertIn(self.tag2, post.tags.all())

    def test_get_summary_method(self):
        # Prueba el método get_summary
        long_content = "This is a very long content for testing the summary method. It should be truncated after a certain number of words."
        post = Post.objects.create(
            titulo='Summary Test Post',
            contenido=long_content,
            autor=self.user,
            category=self.category
        )
        summary = post.get_summary(num_words=10)
        expected_summary = "This is a very long content for testing the summary..."
        self.assertEqual(summary, expected_summary)
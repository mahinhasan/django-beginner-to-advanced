from .models import Post
from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'mhblog',
            email = 'mh@gmail.com',
            password = 'mhblog'
        )

        self.post = Post.objects.create(
            title = 'Every man has problem',
            body = 'problem is a part of human body',
            author = self.user,
        )
    
    def test_string_representation(self):
        post = Post(title='Every man has problem')
        self.assertEqual(str(post),post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/post/1/detail')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','Every man has problem'),

        self.assertEqual(f'{self.post.author}','mhblog')

        self.assertEqual(f'{self.post.body}','problem is a part of human body')
    

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code,200)

        self.assertContains(response,'problem is a part of human body')

        self.assertTemplateUsed(response,'blog/index.html')


    def test_post_detail_view(self):
        response = self.client.get('/post/1/detail')
        no_response = self.client.get('/post/1000/detail')

        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Every man has problem')
        self.assertTemplateUsed(response,'blog/post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('create_post'),{
            'title':'Google is my dream company',
            'body':'I wanted to get job at google',
            'author':self.user,
        })
        

        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Google is my dream company')
        self.assertContains(response,'I wanted to get job at google')

    def test_post_update_view(self):
        response = self.client.post(reverse('edit', args='1'), {
        'title': 'Updated title',
        'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertEqual(response.status_code, 200)

    
from django.test import SimpleTestCase
from django.urls import reverse , resolve
from .views import HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_hompage_template(self):
        self.assertTemplateUsed(self.response,'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response,'HomePage')
    
    def test_homepage_doesnot_contain_incorrect_html(self):
        self.assertNotContains(
            self.response,'I am sure I am not there.'
        )
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        # print(view)
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
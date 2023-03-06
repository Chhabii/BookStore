from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
# Create your models here.
class Book(models.Model):
    #id: A unique identifier for the book, generated automatically as a UUID (Universally Unique Identifier) field.
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    cover = models.ImageField(upload_to='covers/',blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id'],name='id_index'),
        ]
        #special_status permission is a custom permission defined specifically for the Book model, and it does not have any special meaning in Django by default
        permissions = [
            ('special_status','Can read all books'),
        ]


    def __str__(self):
        return self.title
    # for individual instance, returns the url patterns 
    # The get_absolute_url method is defined to return the URL pattern for the detail view of a specific book instance, which is named 'book_detail' and takes the id of the book as an argument.
    def get_absolute_url(self):
        return reverse('book_detail',args=[str(self.id)])

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete = models.CASCADE,
        related_name='reviews', #. The related_name='reviews' argument creates a reverse relation on the Book model, allowing you to access all reviews for a particular book using book.reviews.all().
                                #it's a good practice to use it in cases where you have multiple foreign keys to the same model. 
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.review
    
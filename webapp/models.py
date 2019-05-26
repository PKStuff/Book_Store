from django.db import models
from django.contrib.auth.admin import User

class Books(models.Model):

    Subject_Choices = [
        ('Python','Python'),
        ('C','C'),
        ('C++','C++'),
        ('Java','Java'),
        ('C#','C#'),
        ('Scala','Scala'),
        ('PHP','PHP'),
        ('JavaScript','JavaScript'),
        ('jQuery','jQuery'),
        ('SQL','SQL'),
        ('HTML','HTML'),
        ('CSS','CSS'),
        ('other', 'other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication = models.CharField(max_length=100)
    edition = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='books/')
    front_page = models.ImageField(upload_to='images/',null=True)
    more_info = models.TextField(blank=True)
    related_to = models.CharField(max_length=200, choices=Subject_Choices, default='other', blank=False)

    def __str__(self):
        return self.book_name

class Review(models.Model):

    Book_Rating = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]

    Book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, choices=Book_Rating)
    review = models.TextField()

    def __str__(self):
        return self.Book.book_name + "--"+self.user.username


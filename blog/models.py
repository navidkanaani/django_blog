from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    img_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}, {self.date}, {self.author}, {self.tag}"

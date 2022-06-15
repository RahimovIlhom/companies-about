from django.db import models


# category model
class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='category_image/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Company(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='imgs/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    requirement = models.TextField(max_length=300)
    salary = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.title


# comments Model

class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
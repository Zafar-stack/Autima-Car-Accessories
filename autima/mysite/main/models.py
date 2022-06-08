from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Цвета"
        verbose_name_plural = "цвета"

    def __str__(self):
        return self.title


class Product (models.Model):
    title = models.CharField(max_length=300)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    discount = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.title


class About_company (models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    advantages = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    what_we_do = models.CharField(max_length=300)
    desc1 = models.TextField()
    logo1 = models.ImageField(upload_to='upload')
    mission = models.CharField(max_length=300)
    desc2 = models.TextField()
    logo2 = models.ImageField(upload_to='upload')
    history = models.CharField(max_length=300)
    desc3 = models.TextField()
    logo3 = models.ImageField(upload_to='upload')

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "о компании"

    def __str__(self):
        return self.title


class Blog_category(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')

    class Meta:
        verbose_name = "Категории публикаций"
        verbose_name_plural = "категории публикаций"

    def __str__(self):
        return self.title


class Blog (models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=None, null=True)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Blog_category, on_delete=models.CASCADE)
    short_description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    description = models.TextField()

    class Meta:
        verbose_name = "Публикации"
        verbose_name_plural = "публикации"

    def __str__(self):
        return self.title


class FAQ (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "часто задаваемые вопросы"

    def __str__(self):
        return self.title


class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password_email = models.CharField(max_length=200)
    birthdate = models.DateTimeField()

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "информация о пользователе"

    def __str__(self):
        return self.title


class Service_type (models.Model):
    title = models.CharField(max_length=300)
    service_contains = models.TextField()
    logo = models.ImageField(upload_to='upload')

    class Meta:
        verbose_name = "Категории услуг"
        verbose_name_plural = "категории услуг"

    def __str__(self):
        return self.title



class Services (models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    service_types = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    service_types_description = models.CharField(max_length=200)
    offers = models.CharField(max_length=200)
    service_price = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "услуги"

    def __str__(self):
        return self.title
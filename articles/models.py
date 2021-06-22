from django.db import models
from datetime import date

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        "Название категории", max_length=150, blank=False, unique=True
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField("Название статьи", max_length=150, blank=False)
    description = models.TextField("Описание", max_length=150, blank=False)
    date = models.DateField("Дата статьи", default=date.today, blank=False)
    image = models.ImageField("Изображения", blank=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE, blank=False
    )

    def __str__(self):
        return self.title

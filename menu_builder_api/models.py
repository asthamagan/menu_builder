from django.db import models


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class Items(models.Model):
    title = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'


class Modifiers(models.Model):
    title = models.CharField(max_length=200)
    items = models.ForeignKey(Items, related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Modifiers'
        verbose_name_plural = 'Modifiers'


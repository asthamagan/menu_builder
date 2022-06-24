from django.db import models


# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class Items(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    section = models.ForeignKey(Section, related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'


class Modifiers(models.Model):
    Modifiers_description = models.CharField(max_length=200)
    items = models.ManyToManyField(Items)

    class Meta:
        verbose_name = 'Modifiers'
        verbose_name_plural = 'Modifiers'


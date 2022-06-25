from django.db import models


# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Section'


class Items(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    section = models.ForeignKey(Section, related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'


class Modifiers(models.Model):
    modifiers_description = models.CharField(max_length=200)
    items = models.ManyToManyField(Items, related_name='modifiers')

    class Meta:
        verbose_name = 'Modifiers'
        verbose_name_plural = 'Modifiers'


from django.db import models


# Create your models here.

class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.Name


class Element(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Element'

    def __str__(self):
        return self.Name


class Rune(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)
    Density = models.IntegerField(null=False)
    Image = models.CharField(max_length=200)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Element = models.ForeignKey(Element, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Rune'

    def __str__(self):
        return self.Name


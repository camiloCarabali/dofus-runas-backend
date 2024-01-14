from django.db import models


# Create your models here.

class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.Name


class Characteristic(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Characteristic'

    def __str__(self):
        return self.Name


class Rune(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)
    Density = models.IntegerField(null=True)
    Level = models.IntegerField(null=False)
    Effect = models.IntegerField(null=True)
    Image = models.CharField(max_length=200)
    OverMax = models.IntegerField(null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Rune'

    def __str__(self):
        return self.Name

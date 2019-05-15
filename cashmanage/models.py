from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Subcategory(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Account(models.Model):
    name = models.CharField(max_length=128)
    cash_amount = models.IntegerField()


class AccountBalance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()

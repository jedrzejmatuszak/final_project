from django.db import models

CHOICES = (
    ('1', 'Wpływ'),
    ('2', 'Wydatek'),
    # ('3', 'Przeksięgowanie')
)


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=128)
    cash_amount = models.FloatField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    date = models.DateField(auto_now_add=True)
    options = models.TextField(default='2', choices=CHOICES)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    amount = models.FloatField()
    description = models.TextField()

import sys
print('came to models.py')
try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Write your model here
class User(models.Model):
    f_name = models.CharField(max_length=20)
    m_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=120)
    gender = models.CharField(max_length=7)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    account_type = models.CharField(max_length=10)
    account_number = models.IntegerField()
    balance = models.FloatField()

    def __str__(self):
        return f"{self.owner.f_name} Ac.No:({self.account_number})  Type: {self.account_type}"


# class Statement(models.Model):
#     st_owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account')

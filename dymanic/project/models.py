from django.db import models




class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Birth = models.DateField()
    dni = models.IntegerField()
    Phone = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __unicode__(self):
        return self.dni


class Product(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    description = models.DateField()
    unit_price = models.IntegerField()
    image = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ManyToManyField(Client)






    
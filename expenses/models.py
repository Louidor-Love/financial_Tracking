from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating fields
    """
    description = models.TextField(max_length=255)
    class Meta:
        abstract = True

class Product(TimeStampedModel):
    TYPE_CHOICES = [
        ('greengorcer', 'greengorcer'),
        ('butcher shop', 'butcher shop'),
        ('condiment', 'condiment'),
        ('Bakery', 'Bakery'),
        ('Rice/Noodles', 'Rice/Noodles'),
        ('Other', 'Other'),
    ]
    name =  models.CharField(max_length=255)
    image =  models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES, 
        default='Other'
    )
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=0)

    #def __str__(self):
    #    if self.name:
    #        return f" name of the product  : {self.name} //   type : {self.type}"
    #    else:
    #        return f"name not found but type is: - ${self.type}"
   

class Expenses(models.Model):
    created =  models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_total = models.DecimalField(max_digits=5, decimal_places=2)

    # def __str__(self):
    #     return f"  name of the product  : {self.product.name} //  price : {self.price_total}"
    def get_product_name(self):
        return  self.product.name 

class Detail_Expenses(TimeStampedModel):
    title = models.CharField(max_length=200,blank=True, null=True)
    expenses = models.ForeignKey(Expenses, on_delete=models.CASCADE)

    def __str__(self):
        return f"   {self.expenses.product.name} - {self.title}"
  

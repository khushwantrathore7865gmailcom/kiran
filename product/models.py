from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    table_of_Content = models.TextField()
    additional = models.TextField(default="")
    single_user = models.IntegerField()
    multi_user = models.IntegerField()
    cooperate_user = models.IntegerField()
    data_pack = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Clients(models.Model):
    username = models.CharField(max_length=100)
    company = models.CharField(max_length=250)
    position = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.username}"


class Order(models.Model):
    customer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    liscence = models.CharField(max_length=100)
    pay = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer}"


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField()
    company = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name}_{self.email}"


class Inquiry(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField()
    company = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE,default="")

    def __str__(self):
        return f"{self.first_name}_{self.email}"


class Requestforsample(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField()
    company = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE,default="")

    def __str__(self):
        return f"{self.first_name}_{self.email}"


class Talk_to_Analyst(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField()
    company = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE,default="")

    def __str__(self):
        return f"{self.first_name}_{self.email}"


class Customization(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField()
    company = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE,default="")

    def __str__(self):
        return f"{self.first_name}_{self.email}"


class OrderHistory(models.Model):
    customer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()

from django.db import models

# Users модель
class Users(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    TCUSERNAME = models.CharField(max_length=255, unique=True)
    TCPASSWORD = models.CharField(max_length=255)
    TCGENDER = models.CharField(max_length=1, choices=GENDER_CHOICES)
    TCEMAIL = models.EmailField(unique=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.TCUSERNAME


# infoCUBranch модель
class InfoCUBranch(models.Model):
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=False)
    address = models.TextField()
    phone = models.DecimalField(max_digits=15, decimal_places=0)
    latitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)  # Өргөрөг
    longitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)  # Уртраг
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# InfoProduct модель
class InfoProduct(models.Model):
    itemCode = models.DecimalField(max_digits=10, decimal_places=0, unique=True)
    itemName = models.CharField(max_length=255)
    itemBillName = models.CharField(max_length=255)
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemName


# History модель
class History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    infoProducts = models.ManyToManyField(InfoProduct, help_text="Бараа",  related_name='history_products')
    infoCUBranch = models.ForeignKey(InfoCUBranch, on_delete=models.CASCADE)
    totalPrice = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    isPay = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History {self.pk} by {self.user.TCUSERNAME}"

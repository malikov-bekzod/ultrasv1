from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return self.name


class Gender(models.TextChoices):
    not_gender = ("n", "not provided")
    male = ("m","male")
    female = ("f", "female")
    other = ("o", "other")


class Color(models.TextChoices):
    not_color = ("n", "not provided")
    red = ("r", "Red")
    green = ("g", "Green")
    blue = ("b", "Blue")
    yellow = ("y", "Yellow")
    cyan = ("c", "Cyan")
    magenta = ("m", "Magenta")
    white = ("w", "White")
    black = ("k", "Black")


class Size(models.TextChoices):
    not_size = ("n", "not provided")
    XS = ("XS",)
    S = ("S",)
    M = ("M",)
    L = ("L",)
    XL = ("XL",)
    XXL = ("XXL",)
    XXXL = ("XXXL",)


class ClothingType(models.TextChoices):
    not_type = "not provided"
    JACKET = "Jacket"
    JEANS = "Jeans"
    SHORTS = "Shorts"
    T_SHIRT = "T-shirt"
    DRESS = "Dress"
    SKIRT = "Skirt"
    SWEATER = "Sweater"
    COAT = "Coat"
    SUIT = "Suit"
    BLAZER = "Blazer"
    HOODIE = "Hoodie"
    CARDIGAN = "Cardigan"
    TANK_TOP = "Tank Top"
    LEGGINGS = "Leggings"
    TRACKSUIT = "Tracksuit"
    UNDERWEAR = "Underwear"
    SOCKS = "Socks"
    CAP = "Cap"
    HAT = "Hat"


class Brands(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return f"{self.name}"

    # NIKE = "Nike"
    # ADIDAS = "Adidas"
    # PUMA = "Puma"
    # UNDER_ARMOUR = "Under Armour"
    # THE_NORTH_FACE = "The North Face"
    # GUCCI = "Gucci"
    # PRADA = "Prada"
    # ARMANI = "Armani"
    # CALVIN_KLEIN = "Calvin Klein"
    # GAP = "Gap"

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=5, choices=Color.choices, default=Color.not_color)
    size = models.CharField(max_length=5, choices=Size.choices, default=Size.not_size)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    brand = models.ForeignKey(Brands, on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField(default=0)
    types = models.CharField(max_length=50, choices=ClothingType.choices,default=ClothingType.not_type)
    image = models.ImageField(upload_to="shop/product/")
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.not_gender)
    viewed = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return f"{self.product.name} + {self.user.first_name}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return f"{self.product.name} + {self.user.first_name}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return f"{self.product.name} + {self.user.first_name}"

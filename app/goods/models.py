from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Найменування")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = "Категорію"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Найменування")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Зображення')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Ціна')
    discont = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Знижка в %')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name="Кількість")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Кількість - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discont:
            return round(self.price - self.price*self.discont/100, 2)
        
        return self.price
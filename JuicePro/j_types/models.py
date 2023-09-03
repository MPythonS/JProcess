from django.db import models


# Create your models here.
# modelis sulčių tipams (t.y. iš ko gaminama sultys (Vaisių, daržovių, vaisių ir daržovių, uogų, vaisių ir uogų, daržovių ir uogų)
class JuiceTypes(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Sulčių tipas')
    active = models.BooleanField(default=True, verbose_name='Aktyvus')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')
    updated = models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Sulčių tipas'
        verbose_name_plural = 'Sulčių tipai'


pass


# klasė nurodanti iš kokių konkrečių vaisių gaminama sultys
class JuiceFruits(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Vaisiai')
    active = models.BooleanField(default=True, verbose_name='Aktyvus')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')
    updated = models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Vaisiai'
        verbose_name_plural = 'Vaisiai'


pass


# klasė nurodanti iš kokių konkrečių daržovių gaminama sultys
class JuiceVegetables(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Daržovės')
    active = models.BooleanField(default=True, verbose_name='Aktyvus')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')
    updated = models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Daržovės'
        verbose_name_plural = 'Daržovės'


pass


# klasė nurodanti iš kokių konkrečių uogų gaminama sultys
class JuiceBerries(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Uogos')
    active = models.BooleanField(default=True, verbose_name='Aktyvus')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')
    updated = models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Uogos'
        verbose_name_plural = 'Uogos'


pass


class Package(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Pakuotės tipas')
    active = models.BooleanField(default=True, verbose_name='Aktyvus')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Kaina')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')
    updated = models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Pakuotės tipas'
        verbose_name_plural = 'Pakuotės tipai'


pass


class Services(models.Model):
    name = models.CharField(max_length=256, null=False, blank=True, verbose_name='Paslaugos tipas')
    active = models.BooleanField(default=True, verbose_name='Aktyvus')
    unit = models.CharField(max_length=30, null=False, blank=False, verbose_name='Vienetas')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Kaina')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')
    updated = models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Paslaugos tipas'
        verbose_name_plural = 'Paslaugų tipai'


pass

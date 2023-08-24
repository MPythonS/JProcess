from django.db import models

from j_types.models import JuiceTypes, JuiceFruits, JuiceBerries, JuiceVegetables, Package, Services


# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='Užsakymo nr.')
    order_date = models.DateField(verbose_name='Užsakymo Data')
    order_time = models.TimeField(verbose_name='Užsakymo Laikas')
    order_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Suma')
    ORDER_STATUS_CHOICES = (
        ('Priimtas', 'Priimtas'),
        ('Atšauktas', 'Atšauktas'),
        ('Vykdomas', 'Vykdomas'),
        ('Atliktas', 'Atliktas'),
        ('Pranešimas išsiųstas', 'Pranešimas išsiųstas'),
        ('Apmokėtas', 'Apmokėtas'),
        ('Atsiimtas', 'Atsiimtas'),
        ('Užbaigtas', 'Užbaigtas'),
    )
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, verbose_name='Užsakymo Būsena')
    order_notes = models.CharField(max_length=200, verbose_name='Pastabos')
    j_name = models.ForeignKey(JuiceTypes, on_delete=models.CASCADE, verbose_name='Sultys')
    f_name = models.ForeignKey(JuiceFruits, on_delete=models.CASCADE, verbose_name='Vaisiai')
    b_name = models.ForeignKey(JuiceBerries, on_delete=models.CASCADE, verbose_name='Uogos')
    v_name = models.ForeignKey(JuiceVegetables, on_delete=models.CASCADE, verbose_name='Daržovės')
    package_name = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='Pakuotės tipas')
    package_count = models.IntegerField(verbose_name=' Pakuotės Kiekis')
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Paslauga')
    service_count = models.IntegerField(verbose_name='Kiekis')

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'
        ordering = ['order_id']

from django.db import models

from orders.models import Order


# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(
        primary_key=True,
        verbose_name='Kliento nr.'
    )
    customer_name = models.CharField(
        max_length=200,
        verbose_name='Kliento vardas'
    )
    customer_surname = models.CharField(
        max_length=200,
        verbose_name='Kliento pavardė'
    )
    customer_phone = models.CharField(
        max_length=200,
        verbose_name='Kliento tel. nr.'
    )
    customer_email = models.EmailField(
        max_length=200,
        verbose_name='Kliento el. paštas'
    )
    customer_address = models.CharField(
        max_length=200,
        default='-',
        verbose_name='Kliento adresas'
    )
    customer_city = models.CharField(
        max_length=200,
        default='-',
        verbose_name='Kliento miestas'
    )
    customer_postal_code = models.CharField(
        max_length=200,
        default='-',
        verbose_name='Kliento pašto kodas '
    )
    customer_notes = models.CharField(
        max_length=200,
        default='-',
        verbose_name='Pastabos'
    )

    def __str__(self):
        return f"{self.customer_name} {self.customer_surname}"

    class Meta:
        verbose_name = 'Klientas'
        verbose_name_plural = 'Klientai'

class Payment(models.Model):
    payment_id = models.AutoField(
        primary_key=True,
        verbose_name='Mokėjimo nr.'
    )
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Užsakymo nr.'
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Klientas'
    )
    payment_date = models.DateField(
        verbose_name='Mokėjimo data'
    )
    payment_time = models.TimeField(
        verbose_name='Mokėjimo laikas'
    )
    PAYMENT_TYPE_CHOICES = (
        ('Banko pavedimu', 'Banko pavedimu'),
        ('Grynais', 'Grynais'),
        ('Kortele', 'Kortele'),
    )
    payment_type = models.CharField(max_length=20,
                                    choices=PAYMENT_TYPE_CHOICES,
                                    verbose_name='Mokėjimo būdas'
                                    )
    payment_total = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        verbose_name='Suma'
                                        )
    payment_status = models.CharField(
        max_length=20,
        verbose_name='Būsena')
    payment_notes = models.CharField(
        max_length=200,
        verbose_name='Pastabos')


    def __str__(self):
        return str(self.payment_id)

    class Meta:
        verbose_name = 'Mokėjimas'
        verbose_name_plural = 'Mokėjimai'
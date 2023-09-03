from django.db import models


from j_types.models import JuiceTypes, JuiceFruits, JuiceBerries, JuiceVegetables, Package, Services


# Create your models here.
class Order(models.Model):
    # bus pateikiamas per POST requestą
    order_id = models.AutoField(
        primary_key=True,
        verbose_name='Užsakymo nr.'
    )
    order_date = models.DateField(
        verbose_name='Užsakymo Data',
        help_text='Pasirinkite užsakymo datą'
    )
    order_time = models.TimeField(
        verbose_name='Užsakymo Laikas',
        help_text='Pasirinkite užsakymo laiką'
    )
    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE,
        verbose_name='Klientas'
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Suma',
        default=1.00,
        help_text='Suma (koreaguojama)'
    )
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
    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        verbose_name='Užsakymo Būsena',
        help_text='Pasirinkite užsakymo būseną'
    )
    # order_notes neprivalomas laukas todėl blank=True, o kad nebūtų tuščias, todėl default='-' (minus)
    order_notes = models.CharField(
        max_length=200,
        verbose_name='Pastabos',
        blank=True,
        default='-'
    )
    j_name = models.ManyToManyField(
        JuiceTypes,
        verbose_name='Sultys',
        help_text='Sulčių tipas'
    )
    f_name = models.ManyToManyField(
        JuiceFruits,
        verbose_name='Vaisiai',
        blank=True,
        help_text='pasirinkite vieną ar kelis vaisius'
    )
    b_name = models.ManyToManyField(
        JuiceBerries,
        verbose_name='Uogos',
        blank=True,
        help_text='pasirinkite vieną ar kelias uogas'
    )
    v_name = models.ManyToManyField(
        JuiceVegetables,
        verbose_name='Daržovės',
        blank=True,
        help_text='pasirinkite vieną ar kelias daržoves'
    )
    package_name = models.ManyToManyField(
        Package,
        verbose_name='Pakuotės tipas',
        help_text='Pasirinkite pakuotės tipą'
    )
    # antras pakuotės tipo pasirinkimas
    package_name2 = models.ManyToManyField(
        Package,
        verbose_name='Pakuotės tipas 2',
        blank=True,
        related_name='package_name2',
        help_text='Pasirinkite antrą pakuotės tipą'
                                           )
    package_count = models.IntegerField(
        verbose_name='Pakuotės Kiekis',
        default=1,
        help_text='Gamyba nurodo pakuotės kiekį'
    )
    # antras pakuotės kiekio pasirinkimas antram pakuotės tipui
    package_count2 = models.IntegerField(
        verbose_name='Pakuotės Kiekis 2',
        default=0,
        blank=True,
        null=True,
        help_text='Gamyba nurodo pakuotės kiekį'
    )
    sum_for_package = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Suma už pakuotę',
        default=0.00,
        help_text='Suma (koreaguojama)'
    )
    service_name = models.ManyToManyField(
        Services,
        verbose_name='Paslauga',
        help_text='Pasirinkite vieną ar kelias paslaugas', blank=True
    )
    service_count = models.IntegerField(
        verbose_name='Kiekis',
        blank=True,
        null=True,
        default=0,
        help_text='Paslaugų kiekis'
    )

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'
        ordering = ['order_id']

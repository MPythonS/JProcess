# Generated by Django 4.2.4 on 2023-09-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JuiceBerries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Uogos')),
                ('active', models.BooleanField(default=True, verbose_name='Aktyvus')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')),
            ],
            options={
                'verbose_name': 'Uogos',
                'verbose_name_plural': 'Uogos',
            },
        ),
        migrations.CreateModel(
            name='JuiceFruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Vaisiai')),
                ('active', models.BooleanField(default=True, verbose_name='Aktyvus')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')),
            ],
            options={
                'verbose_name': 'Vaisiai',
                'verbose_name_plural': 'Vaisiai',
            },
        ),
        migrations.CreateModel(
            name='JuiceTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Sulčių tipas')),
                ('active', models.BooleanField(default=True, verbose_name='Aktyvus')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')),
            ],
            options={
                'verbose_name': 'Sulčių tipas',
                'verbose_name_plural': 'Sulčių tipai',
            },
        ),
        migrations.CreateModel(
            name='JuiceVegetables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Daržovės')),
                ('active', models.BooleanField(default=True, verbose_name='Aktyvus')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')),
            ],
            options={
                'verbose_name': 'Daržovės',
                'verbose_name_plural': 'Daržovės',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Pakuotės tipas')),
                ('active', models.BooleanField(default=True, verbose_name='Aktyvus')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Kaina')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')),
            ],
            options={
                'verbose_name': 'Pakuotės tipas',
                'verbose_name_plural': 'Pakuotės tipai',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Paslaugos tipas')),
                ('active', models.BooleanField(default=True, verbose_name='Aktyvus')),
                ('unit', models.CharField(max_length=30, verbose_name='Vienetas')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Kaina')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')),
            ],
            options={
                'verbose_name': 'Paslaugos tipas',
                'verbose_name_plural': 'Paslaugų tipai',
            },
        ),
    ]

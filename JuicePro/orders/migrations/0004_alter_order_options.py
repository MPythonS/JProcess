# Generated by Django 4.2.4 on 2023-09-06 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['order_id'], 'verbose_name': 'Užsakymas', 'verbose_name_plural': 'Užsakymai'},
        ),
    ]

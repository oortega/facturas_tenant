# Generated by Django 2.2.8 on 2020-02-01 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_remove_factura_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='s',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

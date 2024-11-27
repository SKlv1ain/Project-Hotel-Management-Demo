# Generated by Django 5.1.3 on 2024-11-16 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_payment_payment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='core.customer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

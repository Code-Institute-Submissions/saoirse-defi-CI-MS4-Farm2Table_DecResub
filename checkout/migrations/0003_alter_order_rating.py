# Generated by Django 3.2.7 on 2021-10-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20211006_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]

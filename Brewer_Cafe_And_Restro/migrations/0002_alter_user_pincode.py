# Generated by Django 5.0.3 on 2024-03-15 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.ForeignKey(db_column='area_pincode', default='000000', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.area'),
        ),
    ]

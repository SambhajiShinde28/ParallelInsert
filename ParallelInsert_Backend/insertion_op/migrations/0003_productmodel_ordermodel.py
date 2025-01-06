# Generated by Django 5.1.4 on 2025-01-06 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insertion_op', '0002_alter_usermodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Product_Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertion_op.usermodel')),
                ('Product_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertion_op.productmodel')),
            ],
        ),
    ]

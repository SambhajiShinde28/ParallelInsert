# Generated by Django 5.1.4 on 2025-01-06 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insertion_op', '0003_productmodel_ordermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='id',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='id',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='id',
            new_name='Id',
        ),
    ]

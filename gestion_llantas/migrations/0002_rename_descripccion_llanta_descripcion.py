# Generated by Django 4.1.1 on 2022-10-06 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_llantas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='llanta',
            old_name='descripccion',
            new_name='descripcion',
        ),
    ]

# Generated by Django 4.1.6 on 2023-07-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_historique'),
    ]

    operations = [
        migrations.AddField(
            model_name='historique',
            name='annee',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
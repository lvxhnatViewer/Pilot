# Generated by Django 3.2.9 on 2021-12-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcharchive',
            name='Title',
            field=models.CharField(default=None, max_length=500),
        ),
    ]

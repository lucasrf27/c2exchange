# Generated by Django 3.1.7 on 2021-07-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0003_auto_20210719_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(max_length=600, null=True),
        ),
    ]

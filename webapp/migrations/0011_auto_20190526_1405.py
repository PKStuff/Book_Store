# Generated by Django 2.1.7 on 2019-05-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20190525_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='price',
        ),
        migrations.AddField(
            model_name='books',
            name='edition',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 2.1.7 on 2019-05-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_books_related_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='related_to',
            field=models.CharField(choices=[('Python', 'Python'), ('C', 'C'), ('C++', 'C++'), ('Java', 'Java'), ('C#', 'C#'), ('Scala', 'Scala'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('jQuery', 'jQuery'), ('SQL', 'SQL'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('other', 'other')], default='other', max_length=200),
        ),
    ]

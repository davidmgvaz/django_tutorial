# Generated by Django 3.1.4 on 2020-12-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alterfield_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(upload_to='projeto/%Y/'),
        ),
    ]

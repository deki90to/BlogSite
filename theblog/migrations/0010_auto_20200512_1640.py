# Generated by Django 3.0.4 on 2020-05-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_auto_20200512_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='.', upload_to=''),
        ),
    ]

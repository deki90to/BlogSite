# Generated by Django 3.0.4 on 2020-05-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='slika.png', upload_to=''),
        ),
    ]
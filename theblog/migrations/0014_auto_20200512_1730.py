# Generated by Django 3.0.4 on 2020-05-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_auto_20200512_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='https://cdn.pixabay.com/photo/2018/01/16/10/36/mistake-3085712_960_720.jpg', upload_to=''),
        ),
    ]
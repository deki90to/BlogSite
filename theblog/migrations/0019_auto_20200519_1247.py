# Generated by Django 3.0.4 on 2020-05-19 10:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0018_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[400, 200], upload_to=''),
        ),
    ]

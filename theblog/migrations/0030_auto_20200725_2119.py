# Generated by Django 3.0.8 on 2020-07-25 19:19

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0029_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[480, 320], upload_to='BlogSite/media/'),
        ),
    ]

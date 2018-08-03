# Generated by Django 2.0.8 on 2018-08-02 19:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tuites', '0003_auto_20180802_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuite',
            name='liked_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
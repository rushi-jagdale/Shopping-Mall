# Generated by Django 3.0.7 on 2020-09-09 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=100)),
                ('shop_loc', models.CharField(max_length=100)),
                ('shop_state', models.CharField(max_length=100)),
                ('shop_des', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
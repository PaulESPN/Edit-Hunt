# Generated by Django 3.0.3 on 2020-06-28 01:44

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
            name='Edit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('votecounter', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='')),
                ('body', models.TextField()),
                ('icon', models.ImageField(upload_to='images/')),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
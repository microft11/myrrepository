# Generated by Django 5.0.4 on 2024-05-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]

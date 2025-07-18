# Generated by Django 5.2.4 on 2025-07-11 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Links.user')),
            ],
        ),
    ]

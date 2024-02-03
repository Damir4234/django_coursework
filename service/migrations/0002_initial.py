# Generated by Django 5.0.1 on 2024-02-03 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(related_name='mailings', to='service.client', verbose_name='клиенты'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='client',
            field=models.ManyToManyField(related_name='logs', to='service.client', verbose_name='клиент'),
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='mailing_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='service.mailing', verbose_name='рассылка'),
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]

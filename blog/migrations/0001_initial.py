# Generated by Django 5.0.1 on 2024-02-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('overview', models.TextField(blank=True, max_length=350, null=True, verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='', verbose_name='изображение')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('view_counter', models.IntegerField(default=0, verbose_name='кол-во просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]

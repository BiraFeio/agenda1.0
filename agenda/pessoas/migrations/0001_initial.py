# Generated by Django 4.1.4 on 2022-12-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('sobrenome', models.CharField(max_length=60)),
                ('fone', models.IntegerField()),
            ],
        ),
    ]

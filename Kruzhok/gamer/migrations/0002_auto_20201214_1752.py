# Generated by Django 3.1.4 on 2020-12-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talent', models.CharField(max_length=16, verbose_name='talentid')),
                ('mail', models.CharField(max_length=128, verbose_name='mail')),
                ('epicid', models.CharField(max_length=128, verbose_name='epicid')),
                ('overwatchname', models.CharField(max_length=128, verbose_name='overwatch_name')),
            ],
            options={
                'verbose_name': 'Talentovec',
                'verbose_name_plural': 'Talentovci',
            },
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]

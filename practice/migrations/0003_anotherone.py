# Generated by Django 2.0.13 on 2019-07-01 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_auto_20190628_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=30)),
                ('b', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

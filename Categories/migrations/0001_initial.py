# Generated by Django 4.1.2 on 2022-10-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('Categories_name', models.CharField(max_length=10)),
                ('Categories_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applicantdetails',
            fields=[
                ('japplient_app_id', models.IntegerField(primary_key=True, serialize=False)),
                ('japplient_results', models.CharField(max_length=50)),
                ('japplient_passyear', models.IntegerField()),
                ('japplient_qualification', models.CharField(max_length=50)),
                ('japplient_languageflu', models.CharField(max_length=20)),
                ('japplient_status', models.CharField(max_length=20)),
                ('japplient_cv', models.CharField(max_length=50)),
                ('japplient_applicant', models.CharField(max_length=50)),
            ],
        ),
    ]

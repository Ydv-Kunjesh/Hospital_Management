# Generated by Django 4.2.5 on 2023-09-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_appointment_yourage'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memail', models.CharField(max_length=50)),
                ('mphone', models.BigIntegerField()),
                ('maddress', models.CharField(max_length=50)),
                ('mcity', models.CharField(max_length=50)),
                ('mstate', models.CharField(max_length=50)),
                ('mpinno', models.BigIntegerField()),
                ('mdetails', models.CharField(max_length=50)),
            ],
        ),
    ]

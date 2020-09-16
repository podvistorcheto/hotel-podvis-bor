# Generated by Django 3.1.1 on 2020-09-16 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('TWIN', 'TWIN ROOM'), ('DBL', 'DOUBLE ROOM'), ('FAM', 'FAMILY ROOM'), ('DSUI', 'DELUXE SUITE'), ('APT', 'APARTMENT'), ('DAPT', 'DELUXE APARTMENT')], max_length=10)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('children_capacity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

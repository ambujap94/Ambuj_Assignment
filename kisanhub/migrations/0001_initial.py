# Generated by Django 3.0 on 2019-12-09 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('metric', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=4, max_digits=10)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kisanhub.Locations')),
                ('metric', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kisanhub.Metrics')),
            ],
            options={
                'unique_together': {('year', 'month', 'location', 'metric')},
            },
        ),
    ]
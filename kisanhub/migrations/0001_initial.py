# Generated by Django 3.0 on 2019-12-12 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('metric', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=4, max_digits=10)),
                ('date', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kisanhub.Location')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kisanhub.Metric')),
            ],
            options={
                'ordering': ['date'],
                'unique_together': {('date', 'location', 'metric')},
            },
        ),
    ]

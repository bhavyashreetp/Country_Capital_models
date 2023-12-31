# Generated by Django 4.2.1 on 2023-06-19 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('cap_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]

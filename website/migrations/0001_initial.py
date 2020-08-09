# Generated by Django 3.0.6 on 2020-08-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('workers', models.IntegerField()),
                ('date_required', models.DateField()),
            ],
        ),
    ]
# Generated by Django 4.1 on 2022-11-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('college', models.CharField(max_length=122)),
                ('branch', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('question1', models.CharField(max_length=4)),
                ('question2', models.CharField(max_length=4)),
                ('question3', models.CharField(max_length=4)),
                ('question4', models.CharField(max_length=4)),
                ('question5', models.CharField(max_length=4)),
                ('question6', models.CharField(max_length=4)),
                ('question7', models.CharField(max_length=4)),
                ('question8', models.CharField(max_length=4)),
                ('question9', models.CharField(max_length=4)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('college', models.CharField(max_length=122)),
                ('branch', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('problem', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]

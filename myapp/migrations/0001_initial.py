# Generated by Django 4.0.3 on 2022-04-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mahajan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.IntegerField()),
                ('college_name', models.CharField(max_length=90)),
                ('degree', models.CharField(max_length=90)),
                ('branch', models.CharField(max_length=90)),
                ('section_name', models.CharField(max_length=90)),
                ('select_course', models.CharField(choices=[('JAVA', 'java'), ('Python', 'python'), ('C', 'c')], max_length=56)),
            ],
            options={
                'db_table': 'sukritan',
            },
        ),
    ]
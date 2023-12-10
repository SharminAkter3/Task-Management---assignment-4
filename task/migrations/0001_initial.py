# Generated by Django 4.2.7 on 2023-12-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('assigned_date', models.DateTimeField()),
                ('categories', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]

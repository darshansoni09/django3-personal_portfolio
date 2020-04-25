# Generated by Django 3.0.5 on 2020-04-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=100)),
                ('blogDate', models.DateField()),
                ('blogContent', models.TextField()),
            ],
        ),
    ]
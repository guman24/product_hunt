# Generated by Django 2.2 on 2019-12-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('product_desc', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product_icon', models.ImageField(upload_to='images/')),
                ('total_votes', models.IntegerField()),
                ('url', models.TextField()),
            ],
        ),
    ]

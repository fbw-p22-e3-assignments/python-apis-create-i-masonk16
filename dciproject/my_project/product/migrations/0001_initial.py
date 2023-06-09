# Generated by Django 4.2.1 on 2023-05-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=50)),
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_category', models.CharField(max_length=50)),
                ('product_description', models.TextField(max_length=250)),
                ('product_image_url', models.URLField()),
                ('product_price', models.PositiveIntegerField()),
            ],
        ),
    ]

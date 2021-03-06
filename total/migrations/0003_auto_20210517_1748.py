# Generated by Django 3.1.7 on 2021-05-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total', '0002_auto_20210414_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productname',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

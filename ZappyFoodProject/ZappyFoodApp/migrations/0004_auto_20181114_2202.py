# Generated by Django 2.1.1 on 2018-11-14 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZappyFoodApp', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('products', models.ManyToManyField(blank=True, to='ZappyFoodApp.AddProduct')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ZappyFoodApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delievery_address', models.CharField(max_length=200, null='True')),
                ('status', models.IntegerField(null='True')),
                ('pid', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='ZappyFoodApp.AddProduct')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer',
            field=models.OneToOneField(null='True', on_delete=django.db.models.deletion.CASCADE, to='ZappyFoodApp.User'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_address',
            field=models.CharField(max_length=400, null='True'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=20, null='True'),
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-06 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_app', '0003_rename_name_carbrand_brand_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_registration', models.DateTimeField(auto_now_add=True)),
                ('odometer', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_app.carbrand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_app.carmodel')),
            ],
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_car_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_drive',
            field=models.CharField(choices=[('FRO', 'Передний'), ('REA', 'Задний'), ('ALL', 'Полный')], default='FRO', max_length=3, verbose_name='Тип привода'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_engine_type',
            field=models.CharField(choices=[('GAS', 'Бензин'), ('DIE', 'Дизель'), ('ELE', 'Электро')], default='GAS', max_length=3, verbose_name='Тип двигателя'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_transmission_type',
            field=models.CharField(choices=[('MAN', 'Механика'), ('AUT', 'Автомат'), ('ROB', 'Робот'), ('VAR', 'Вариатор')], default='MAN', max_length=3, verbose_name='Тип трансмиссии'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_wheel',
            field=models.CharField(choices=[('LEF', 'Левый'), ('RIG', 'Правый')], default='LEF', max_length=3, verbose_name='Руль'),
        ),
    ]
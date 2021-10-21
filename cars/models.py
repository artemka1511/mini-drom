from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class City(models.Model):
    city_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.city_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)
    brand_country = models.CharField(max_length=30)
    brand_history = models.TextField()
    brand_logo = models.ImageField(verbose_name='Логотип', upload_to='logo/', null=True)

    def __str__(self):
        return self.brand_name


class Model(models.Model):
    model_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.model_name


gasoline = 'GAS'
diesel = 'DIE'
electro = 'ELE'

ENGINE_TYPE = [(gasoline, 'Бензин'),
               (diesel, 'Дизель'),
               (electro, 'Электро')]

manual = 'MAN'
auto = 'AUT'
robot = 'ROB'
variator = 'VAR'

TRANSMISSION_TYPE = [(manual, 'Механика'),
                     (auto, 'Автомат'),
                     (robot, 'Робот'),
                     (variator, 'Вариатор')]


front = 'FRO'
rear = 'REA'
all = 'ALL'

DRIVE_TYPE = [(front, 'Передний'),
              (rear, 'Задний'),
              (all, 'Полный')]

red = 'RED'
green = 'GRE'
blue = 'BLU'
white = 'WHI'
black = 'BLA'
yellow = 'YEL'


COLOR_TYPE = [(red, 'Красный'),
              (green, 'Зелёный'),
              (blue, 'Синий'),
              (white, 'Белый'),
              (black, 'Чёрный'),
              (yellow, 'Жёлтый')]

left = 'LEF'
right = 'RIG'

WHEEL_TYPE = [(left, 'Левый'),
              (right, 'Правый')]


class Car(models.Model):
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Марка')
    car_model = ChainedForeignKey(Model,
                                  chained_field="car_brand",
                                  chained_model_field="model_brand_id",
                                  show_all=False,
                                  auto_choose=True,
                                  sort=True,
                                  on_delete=models.CASCADE,
                                  verbose_name='Модель')
    car_year = models.IntegerField(verbose_name='Год выпуска')
    car_price = models.IntegerField(verbose_name='Стоимость автомобиля')
    car_engine_type = models.CharField(max_length=3, choices=ENGINE_TYPE, default=gasoline, verbose_name='Тип двигателя')
    car_engine_capacity = models.FloatField(max_length=3, verbose_name='Объём')
    car_engine_power = models.IntegerField(verbose_name='Мощность л.с.')
    car_transmission_type = models.CharField(max_length=3, choices=TRANSMISSION_TYPE, default=manual, verbose_name='Тип трансмиссии')
    car_drive = models.CharField(max_length=3, choices=DRIVE_TYPE, default=front, verbose_name='Тип привода')
    car_color = models.CharField(max_length=3, choices=COLOR_TYPE, default=white, verbose_name='Цвет')
    car_mileage = models.IntegerField(verbose_name='Пробег')
    car_wheel = models.CharField(max_length=3, choices=WHEEL_TYPE, default=left, verbose_name='Руль')
    car_vin = models.IntegerField(unique=True, verbose_name='VIN номер')
    car_description = models.TextField(verbose_name='Описание')
    car_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    car_date_create = models.DateTimeField(auto_now_add=True)
    car_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.car_brand} {self.car_model}'

    def get_absolute_url(self):
        return f'/{self.id}'


class Images(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='car_photo', verbose_name='Фото', null=True)







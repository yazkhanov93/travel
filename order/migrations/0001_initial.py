# Generated by Django 4.2 on 2023-04-23 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0001_initial'),
        ('tour', '0002_tour_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('night', models.IntegerField(default=1, verbose_name='Количество ночей')),
                ('person_count', models.IntegerField(default=1, verbose_name='Количество человек')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_order', to='hotel.hotel', verbose_name='Отель')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_order', to='tour.tour', verbose_name='Тур')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]

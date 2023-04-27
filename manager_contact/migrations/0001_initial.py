# Generated by Django 4.2 on 2023-04-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Менеджер')),
                ('whatsapp', models.CharField(max_length=255, verbose_name='whatsapp_link')),
            ],
            options={
                'verbose_name_plural': 'Менеджер WhatsApp',
            },
        ),
    ]
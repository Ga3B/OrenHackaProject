# Generated by Django 3.0.7 on 2020-06-12 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(max_length=20, verbose_name='название статуса')),
            ],
        ),
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='Окрас животного')),
                ('weight', models.FloatField(verbose_name='Вес животного')),
                ('PhotoUrl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(verbose_name='Время подачи заявки')),
                ('description', models.TextField(null=True, verbose_name='Комментарий')),
                ('geotag', models.TextField(verbose_name='Геометка')),
                ('status', models.CharField(max_length=20, verbose_name='Статус')),
                ('photoURL', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование приюта')),
                ('adres', models.CharField(max_length=150, verbose_name='Адрес приюта')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_id', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_transfer', models.DateTimeField(verbose_name='Дата передачи животного')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Animals', verbose_name='Животное')),
                ('request_id', models.ForeignKey(on_delete=models.SET('#0'), to='MainApp.Request', verbose_name='№ заявки')),
                ('status_id', models.ForeignKey(on_delete=models.SET('Неизвестно'), to='MainApp.Animal_status', verbose_name='Статус')),
                ('user_id', models.ForeignKey(on_delete=models.SET('Админ'), to='MainApp.Visitor', verbose_name='Ловец')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.Visitor', verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Released_animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_relise', models.DateTimeField(verbose_name='Дата выпуска')),
                ('geotag_relise', models.TextField(verbose_name='Место выпуска')),
                ('number_of_chip', models.CharField(max_length=50, verbose_name='Код чипа')),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Animals')),
            ],
        ),
        migrations.CreateModel(
            name='Animal_story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=50, verbose_name='Операции')),
                ('animals_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Animals')),
            ],
        ),
    ]
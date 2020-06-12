from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vk_id = models.TextField()


# Животное
class Animals(models.Model):
    color = models.CharField("Окрас животного", max_length=20)
    weight = models.FloatField("Вес животного")
    PhotoUrl = models.TextField()

# история операций


class Animal_story(models.Model):
    animals_id = models.ForeignKey(Animals, on_delete=models.CASCADE)
    operation = models.CharField("Операции", max_length=50)


# Заявка на отлов


class Request(models.Model):
    dateTime = models.DateTimeField("Время подачи заявки")
    user_id = models.ForeignKey(Visitor, on_delete=models.DO_NOTHING,
                                verbose_name="Пользователь", )
    description = models.TextField("Комментарий", null=True)
    geotag = models.TextField("Геометка")
    status = models.CharField("Статус", max_length=20)
    photoURL = models.TextField(null=True)

# статус животного


class Animal_status(models.Model):
    name_status = models.CharField("название статуса", max_length=20)

    def __str__(self):
        return self.name_status

# акт приема-передачи


class Transfer(models.Model):
    animal_id = models.ForeignKey(Animals, on_delete=models.CASCADE,
                                  verbose_name="Животное")
    status_id = models.ForeignKey(Animal_status, on_delete=models.SET("Неизвестно"),
                                  verbose_name="Статус")
    request_id = models.ForeignKey(Request, on_delete=models.SET("#0"),
                                   verbose_name="№ заявки")
    user_id = models.ForeignKey(Visitor, on_delete=models.SET("Админ"),
                                verbose_name="Ловец")
    date_of_transfer = models.DateTimeField("Дата передачи животного")
    description = models.TextField(null=True, verbose_name="Описание")

# приют


class Shelter(models.Model):
    name = models.CharField("Наименование приюта", max_length=20)
    adres = models.CharField("Адрес приюта", max_length=150)
    phone = models.CharField("Номер телефона", max_length=12)

# выпущенные животные


class Released_animals(models.Model):
    animal_id = models.ForeignKey(Animals, on_delete=models.CASCADE)
    date_of_relise = models.DateTimeField("Дата выпуска")
    geotag_relise = models.TextField("Место выпуска")
    number_of_chip = models.CharField("Код чипа", max_length=50)

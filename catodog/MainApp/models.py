from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vk_id = models.TextField()


# Животное
class Animals(models.Model):
    color = models.CharField("Окрас животного", max_length=20)
    weight = models.FloatField("Вес животного")
    PhotoUrl = models.ImageField(
        blank=True, upload_to='static/requests/imgAnimal')
    special_signs = models.CharField("Особые приметы", max_length=20)
    sort_animal = models.CharField("Вид животного", max_length=20)
    gender = models.CharField("Пол", max_length=20)
    behavior = models.CharField(
        "Поведение животного", max_length=40, null=True)
    chip = models.CharField("Чип животного", max_length=50, null=True)

    # def get_absolute_url(self):
    #     return reverse('animal_detail', kwargs={'id': self.pk})

    # def get_absolute_url(self):
    #     return reverse('MainApp/act.html', kwargs={'id': self.pk})

    def __str__(self):
        return self.chip


class Lost_animals(models.Model):

    animal_id = models.ForeignKey(
        Animals, on_delete=models.SET('NULL'), related_name='animals_id')
    user_id = models.ForeignKey(
        User, on_delete=models.SET('NULL'), related_name='user_id')
    date = models.DateTimeField()


# история операций
class Animal_story(models.Model):
    animals_id = models.ForeignKey(Animals, on_delete=models.CASCADE)
    operation = models.CharField("Операции", max_length=50)


class Status(models.Model):
    name = models.CharField('Статус', max_length=20)

    def __str__(self):
        return self.name


# Заявка на отлов
class Request(models.Model):
    dateTime = models.DateTimeField("Время подачи заявки")
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                verbose_name="Пользователь")
    description = models.TextField("Комментарий", null=True)
    geotag = models.TextField("Геометка")

    status = models.ForeignKey(Status, on_delete=models.SET(
        "Неизвестно"), verbose_name="Статус", max_length=20)
    photoURL = models.ImageField(
        blank=True, upload_to='static/requests/imgReq')

    def get_absolute_url(self):
        return reverse('request_detail', kwargs={'id': self.pk})

    def __str__(self):
        return str(self.pk)


# статус животного
class Animal_status(models.Model):
    name_status = models.CharField("название статуса", max_length=20)

    def __str__(self):
        return self.name_status

# приют
class Shelter(models.Model):
    name = models.CharField("Наименование приюта", max_length=20)
    adres = models.CharField("Адрес приюта", max_length=150)
    phone = models.CharField("Номер телефона", max_length=12)
    animals_id = models.ForeignKey(Animals, on_delete=models.SET("Null"), related_name='animal_shelter_ID', null=True)


# акт приема-передачи
class Transfer(models.Model):

    status_id = models.ForeignKey(Animal_status, on_delete=models.SET("Неизвестно"),
                                  verbose_name="Статус")
    request_id = models.ForeignKey(Request, on_delete=models.SET("#0"),
                                   verbose_name="№ заявки")
    user_id = models.ForeignKey(User, on_delete=models.SET("Null"),
                                verbose_name="Ловец")
    date_of_transfer = models.DateTimeField("Дата передачи животного")
    description = models.TextField(null=True, verbose_name="Описание")

    animals_id = models.ForeignKey(Animals, on_delete=models.SET("Null"), related_name='animal_transfer_ID')
    shelter_id = models.ForeignKey(Shelter, on_delete=models.SET("Отсутствует"))

    def __str__(self):
        return str(self.request_id)


# выпущенные животные


class Released_animals(models.Model):
    animal_id = models.ForeignKey(Animals, on_delete=models.CASCADE)
    date_of_relise = models.DateTimeField("Дата выпуска")
    geotag_relise = models.TextField("Место выпуска")
    number_of_chip = models.CharField("Код чипа", max_length=50)

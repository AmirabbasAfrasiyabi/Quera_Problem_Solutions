from django.db import models
from django.core.exceptions import ValidationError
from django_jalali.db import models as jmodels
import jdatetime


class CustomUser(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHERS = 'O'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHERS, 'Others'),
    )
    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256 , choices=GENDER_CHOICES)
    national_code = models.CharField(max_length=10)
    birthday_date = models.DateField()
    ceremony_datetime = models.DateField()
    country = models.CharField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Users'
        app_label = 'Users'
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def get_first_and_last_name(self):
        first, last = self.full_name.split(" ")
        return {"first_name": first, "last_name": last}

    def get_age(self):
        today = jdatetime.date.today()
        b = self.birthday_date
        age = today.year - b.year
        if (today.month, today.day) < (b.month, b.day):
            age -= 1
        return age

    def is_birthday(self):
        today = jdatetime.date.today()
        return today.month == self.birthday_date.month and today.day == self.birthday_date.day
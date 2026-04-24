from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)                # اسم الطالب
    phone = models.CharField(max_length=20)                # رقم الهاتف
    email = models.EmailField(unique=True)                 # البريد الإلكتروني
    major = models.CharField(max_length=100)               # التخصص
    added_date = models.DateField(auto_now_add=True)       # تاريخ الإضافة (يُسجل تلقائيًا)

    def __str__(self):
        return self.name
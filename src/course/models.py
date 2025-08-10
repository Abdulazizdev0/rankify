from django.db import models

# course,yonalish,fakultet


class Yonalish(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Fakultet(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('MBA', 'MBA'),
    ]

    Name = models.CharField(max_length=30)
    F_name = models.CharField(max_length=30)
    M_name = models.CharField(max_length=30)
    p_no = models.IntegerField()
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    roll = models.IntegerField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.Name

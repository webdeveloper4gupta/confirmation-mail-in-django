from django.db import models
course=[("JAVA",'java'),('Python','python'),('C','c')]
# Create your models here.
class mahajan(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    email=models.EmailField(blank=True)
    college_name=models.CharField(max_length=90)
    degree=models.CharField(max_length=90)
    branch=models.CharField(max_length=90)
    section_name=models.CharField(max_length=90)
    select_course=models.CharField(max_length=56,choices=course)
    class Meta:
        db_table="sukritan"
    def __str__(self):
        return self.name



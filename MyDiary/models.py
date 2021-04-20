from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Patient(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    apt = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date(2021,3,3))
    mobile = models.CharField(max_length=100)
    home_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE, related_name="list_patient")

    def __str__(self):
        return self.First_Name+" "+self.Last_Name

#Problem Classification Scheme:

# Psychosocial, Environmental
class Scheme(models.Model):
    scheme_name = models.CharField(max_length=100)

    def __str__(self):
        return self.scheme_name

class Domain(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="list_domain")
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, related_name="list_domain")

    def __str__(self):
        return self.name


# Mental Health, abuse
class Problem(models.Model):
    problemName = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="list_problem")

    def __str__(self):
        return "Problem: "+self.problemName+", Priority: "+self.priority

class Modifier(models.Model):
    modifierType = models.CharField(max_length=100) #actual/potential/promotion
    problem_modifier = models.CharField(max_length=100) #individual/community/family
    problems = models.ManyToManyField(Problem)

    def __str__(self):
        return "Modifier: "+self.problem_modifier+", Type: "+self.modifierType

# Domain->Problem->SignAndSymptom => delusions, mood swings
class SignAndSymptom(models.Model):
    symptomName = models.CharField(max_length=100)
    symptomDescription = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="list_symptom")

    def __str__(self):
        return self.symptomName

# Intervention Scheme:
# Case Management, Survillience
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Target(models.Model):
    targetName = models.CharField(max_length=100)
    targetDescription = models.CharField(max_length=100)
    targetNote = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="list_target")

    def __str__(self):
        return self.targetName

# Problem rating scale
class Rating_Scale(models.Model):
    rating_knowledge = models.IntegerField()
    rating_behavior = models.IntegerField()
    rating_status = models.IntegerField()
    note = models.TextField()

    def __str__(self):
        return "Knowledge: "+str(self.rating_knowledge)+" Behavior: "+str(self.rating_behavior)+" Status: "+str(self.rating_status)

class patient_evaluation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="list_patient")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="list_problem")
    rating_scale = models.ForeignKey(Rating_Scale, on_delete=models.CASCADE, related_name="list_rating_scale")
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name="list_target")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="list_category")

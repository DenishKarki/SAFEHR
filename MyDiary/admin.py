from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Domain)
admin.site.register(Problem)
admin.site.register(SignAndSymptom)
admin.site.register(Category)
admin.site.register(Target)
admin.site.register(Rating_Scale)
admin.site.register(Scheme)
admin.site.register(patient_evaluation)
admin.site.register(Modifier)

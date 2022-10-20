from django.contrib import admin

# Register your models here.
from .models import states
admin.site.register (states)
from .models import hospitallist
admin.site.register (hospitallist)
from .models import department
admin.site.register (department)
from .models import user_reg
admin.site.register (user_reg)
from .models import consultation
admin.site.register (consultation)
from .models import doctor_availability
admin.site.register (doctor_availability)
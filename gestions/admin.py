from django.contrib import admin

from gestions.models import Attribution, Course, Employer, Mission, Projet


# Register your models here.
admin.site.register(Employer)
admin.site.register(Projet)
admin.site.register(Attribution)
admin.site.register(Course)
admin.site.register(Mission)
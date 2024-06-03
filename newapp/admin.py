from django.contrib import admin

# Register your models here.
from .models import adminsignupmodel, Newbookmodel, studentsignupmodel, IssuedBook
admin.site.register(adminsignupmodel)
admin.site.register(Newbookmodel)
admin.site.register(studentsignupmodel)
admin.site.register(IssuedBook)

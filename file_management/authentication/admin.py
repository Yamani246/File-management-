from django.contrib import admin
from .models import CustomUser,File,Subject,Department,AcademicYear
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['name']

    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_department_name', 'academic_year']

    def get_department_name(self, obj):
        return obj.department.name

    get_department_name.short_description = 'Department'  

class SectionAdmin(admin.ModelAdmin):
    list_display=['no','year','department']

    def department(self,obj):
        return obj.department.name
    
    def year(self,obj):
        return obj.academic_year.year


class AcademicyearAdmin(admin.ModelAdmin):
    list_display=['year']

admin.site.register(AcademicYear,AcademicyearAdmin)
admin.site.register(CustomUser)
admin.site.register(File)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Department,DepartmentAdmin)
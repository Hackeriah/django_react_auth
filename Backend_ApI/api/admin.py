from django.contrib import admin
from api.models import User,Profile,Category,Course
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ["verified"]
    list_display = ['user', 'full_name', 'verified','bio']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']
    list_editable=['description']


class CourseAdmin(admin.ModelAdmin):
    list_display=[ 'category','description','price','title']
    list_editable=['description','price','title']

admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
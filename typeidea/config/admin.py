from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Link, SideBar
# Register your models here.

@ admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','href','status','weight','created_time')
    fields = ('title','href','status','weight')
    def save_model(self, request, obj, form, change) -> None:
        obj.owner = request.user
        return super(LinkAdmin,self).save_model(request, obj, form, change)


@ admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title','display_type','content','status','created_time')
    fields = ('title','display_type','content','status')
    
    def save_model(self, request, obj, form, change) -> None:
        obj.owner = request.user
        return super(SideBarAdmin,self).save_model(request, obj, form, change)
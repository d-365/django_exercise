from typing import Any
from django.contrib import admin

# Register your models here.
from .models import Post,Category,Tag
from django.utils.html import format_html
from django.urls import reverse

@ admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_nav','created_time')
    fields = ('name','status','is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin,self).save_model(request, obj, form, change)


@ admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_time')
    fields = ('name','status')
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin,self).save_model(request, obj, form, change)

@ admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # admin 后台数据表展示哪些字段
    list_display = ('title','category','status','created_time','operator')
    # admin后台那些字段可以当做链接被点击
    list_display_links=[]
    list_filter =['category']
    search_fields = ['title','category_name']
    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True
    fields = (
        ('category','title'),
        'desc',
        'status',
        'content',
        'tag'

    )

    def operator(self,obj):
        return format_html( 
        '<a href="{}"> 编辑 </a>',
        reverse('admin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request: Any, obj, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super(PostAdmin,self).save_model(request, obj, form, change)

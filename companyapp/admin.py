from django.contrib import admin
from .models import Category, Company, Comment

# Register your models here.
admin.site.register(Category, )


class AdminCompanies(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')


admin.site.register(Company, AdminCompanies)


class AdminComment(admin.ModelAdmin):
    list_display = ('company', 'email', 'comment', 'status')


admin.site.register(Comment, AdminComment)

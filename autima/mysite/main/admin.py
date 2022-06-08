from django.contrib import admin
from main.models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class ColorAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class About_companyAdmin(admin.ModelAdmin):
    pass


class Blog_categoryAdmin(admin.ModelAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    pass


class FAQAdmin(admin.ModelAdmin):
    pass


class UsersAdmin(admin.ModelAdmin):
    pass


class Service_typeAdmin(admin.ModelAdmin):
    pass


class ServicesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(About_company, About_companyAdmin)
admin.site.register(Blog_category, Blog_categoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Service_type, Service_typeAdmin)
admin.site.register(Services, ServicesAdmin)
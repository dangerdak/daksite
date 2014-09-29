from django.contrib import admin
from django.db import models

from blog.models import Post, Category

from pagedown.widgets import AdminPagedownWidget


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'last_modified')
    radio_fields = {'status': admin.HORIZONTAL}

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

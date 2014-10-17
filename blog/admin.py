from django.contrib import admin
from django.db import models
from django.forms import Textarea

from blog.models import Post, Category, Image

from pagedown.widgets import AdminPagedownWidget


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 4}
                           )}
    }
    fields = ('title', 'caption', 'image')


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'last_modified')
    radio_fields = {'status': admin.HORIZONTAL}

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    inlines = [
        ImageInline,
    ]

    fieldsets = [
        (None,      {'fields': ['title', ('status', 'category'), 'body']}),
        ('Advanced',    {'fields': ['slug', 'pub_date'],
                         'classes': ['collapse']}),
    ]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

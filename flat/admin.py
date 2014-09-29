from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm

from pagedown.widgets import AdminPagedownWidget


class MyFlatpageForm(FlatpageForm):

    class Meta:
        widgets = {
            'content': AdminPagedownWidget,
        }


class MyFlatPageAdmin(FlatPageAdmin):
    form = MyFlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)

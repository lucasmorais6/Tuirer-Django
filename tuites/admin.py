from django.contrib import admin
from tuites.models import Tuite


class TuiteAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date_created')
    list_filter = ('author', 'date_created', )

#admin.site.unregister(Tuite)
admin.site.register(Tuite, TuiteAdmin)
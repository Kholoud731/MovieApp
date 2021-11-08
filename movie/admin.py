from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Movie,Category, Cast

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display = ('name', 'active','my_custom_list_display_feild')
    readonly_fields = ('my_custom_list_display_feild',)

    def my_custom_list_display_feild(self, obj):
        total = 100 * (obj.rate / 100)
        return f'{total} %'
    
    my_custom_list_display_feild.short_description = 'Percent of rate'     


    fieldsets = (
        ["Required details" , {"fields": ["name", "description", "language", "category","cast"]}],
        ["Attachments" , {"fields" : ["image","active"]}],
        ["Extra Details" , {"fields" : ["running_time","rate", "my_custom_list_display_feild","release_date"]}] )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Cast)
admin.site.register(Category)

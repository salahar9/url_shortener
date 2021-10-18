from django.contrib import admin
from .models import Visit,ShortUrl
from django.utils.html import format_html

class CountryFilter(admin.SimpleListFilter):
    title = 'country'
    parameter_name = 'country__exact'

    def lookups(self, request, model_admin):
        countries=set(Visit.objects.values_list("country",flat=True))
        country_pair=[[country,country]  for country in countries]
        return country_pair 

    def queryset(self, request, queryset):
        countries=set(Visit.objects.values_list("country",flat=True))

        
        if self.value() != "localhost" and  self.value() in countries:
            return queryset.filter(country__exact=self.value)
        return queryset
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display=["country","country_flag","os","date_of_visit",]
    
    list_filter=[CountryFilter,"date_of_visit","os"]
    @admin.display
    def country_flag(self,obj):
        return format_html(f'<img src="{obj.country.flag}"/>')
    
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display=["alias","long_url","number_of_visits","creation_date"]
    ordering=["-visits"]

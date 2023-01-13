from django.contrib import admin
from .models import *


class SectionLine(admin.TabularInline):
    model = Section
    extra = 0


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name", )}
    inlines = [SectionLine]


class OrdsLine(admin.TabularInline):
    model = Records
    extra = 0

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'view', 'hall_number', 'is_action', 'numb', 'max_numb', 'trainer', 'start_time')
    list_display_links = ('view', )
    list_editable = ('is_action', )
    search_fields = ('name', 'hall_number')
    inlines = [OrdsLine]
    prepopulated_fields = {"slug": ("name", "trainer")}


@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'user', 'start_date', 'is_paid')
    list_display_links = ('section', 'user')
    list_editable = ('is_paid',)
    list_filter = ('is_paid', 'time_create')



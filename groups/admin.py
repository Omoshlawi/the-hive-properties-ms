from django.contrib import admin

from groups.models import Group, GroupProperties


# Register your models here.


class GroupPropertiesInline(admin.TabularInline):
    model = GroupProperties


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'cover_image')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GroupPropertiesInline]

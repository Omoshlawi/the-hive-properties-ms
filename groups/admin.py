from django.contrib import admin

from groups.models import Group, PropertyGroupMemberShip


# Register your models here.


class GroupPropertiesInline(admin.TabularInline):
    model = PropertyGroupMemberShip


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'cover_image', 'tag_list')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GroupPropertiesInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

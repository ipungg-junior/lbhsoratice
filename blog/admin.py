from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Tag, UserAccount
from django.contrib.auth.admin import UserAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)




class CustomUserAdmin(UserAdmin):
    model = UserAccount
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)




admin.site.register(Article, PostAdmin)
admin.site.register(Tag)
admin.site.register(UserAccount)
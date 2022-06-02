from django.contrib import admin

from .models import Note

@admin.register(Note)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'state', 'author', 'important', 'public', 'pub_date')
    fields = (('title', 'author'), 'desc', ('state', 'public', 'important'), 'pub_date')
    search_fields = ('title', 'desc')
    list_filter = ('author', 'important', 'state', 'public')
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'author') or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

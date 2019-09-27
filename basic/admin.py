from django.contrib import admin
from .models import Post
from .models import Rubric

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published')
    #list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Rubric)

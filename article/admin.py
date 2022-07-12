from django.contrib import admin
from .models import Article,Comment
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_filter = ["created_date"]
    search_fields = ["title"]
    list_display = ["id","title","author","created_date"]
    class Meta:
        model = Article

admin.site.register(Comment)
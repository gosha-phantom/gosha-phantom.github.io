from django.contrib import admin
from article.models import Article, Comments

# Register your models here.
class ArticleInline(admin.StackedInline):
	model = Comments
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	fields = ['art_title', 'art_text', 'art_date'] 
	inlines = [ArticleInline]
	list_filter = ['art_date']

admin.site.register(Article, ArticleAdmin)
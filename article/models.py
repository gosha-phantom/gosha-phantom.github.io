from django.db import models

short_text_len = 500
# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = "article"
	art_title = models.CharField(max_length=150)
	art_text = models.TextField()
	art_date = models.DateTimeField()
	art_likes = models.IntegerField(default=0)	#(blank=True, null=True)

	def __str__(self):
		return self.art_title

	def get_short_text(self):
		if len(self.art_text)>short_text_len:
			return self.art_text[:short_text_len] + '...'
		else:
			return self.art_text

class Comments(models.Model):
	class Meta():
		db_table = "comments"

	comm_text = models.TextField()
	comm_article = models.ForeignKey(Article)
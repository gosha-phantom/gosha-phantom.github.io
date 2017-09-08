from django.forms import ModelForm
from article.models import Comments
# from django import forms

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ["comm_text"]
		labels = {"comm_text": "Комментарий"}
		# fields = Comments.comm_text
	# comment = ModelForm.CharField(label='Комментарий')
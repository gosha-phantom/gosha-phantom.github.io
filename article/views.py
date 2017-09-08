from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.template.context_processors import csrf
# Create your views here.
# def basic_one(request):
# 	view = "basic_one"
# 	html = "<html><body>This is %s view</body></html>" %view
# 	return HttpResponse(html)

def template_one(request):
	view = "Hello Python"
	context = {
		'name': view 
	}
	return render(request, "myview1.html", context)

# def test(request):
# 	return HttpResponse("Это тестовая страница!!!")

def hello(request):
	return HttpResponse("Hello Django!")

def templ(request):
	view = "Hello Python 3"
	return render_to_response('myview1.html',{'name': view})

def articles(request):
	context = {
		# 'articles':Article.objects.all()	}
		'articles':Article.objects.order_by("-art_date")}
	return render_to_response('articles.html',context)

def article(request, art_id=1):
	# comment_form = CommentForm
	# context = {'article':Article.objects.get(id=art_id),
	# 	'comments':Comments.objects.filter(comm_article=art_id),
	# 	'form':comment_form}
	# return render_to_response('article.html', context)
	com_form = CommentForm
	args = {}
	args.update(csrf(request))
	args['article'] = Article.objects.get(id=art_id)
	args['comments'] = Comments.objects.filter(comm_article=art_id)
	args['form'] = com_form
	return render_to_response('article.html', args)

def addlike(request, art_id):
	try:
		article = Article.objects.get(id=art_id)
		article.art_likes += 1
		article.save()
	except ObjectDoesNotExist:
		raise Http404
	return redirect('/')

def addcomment(request, art_id):
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.comm_article = Article.objects.get(id=art_id)
			form.save()
		return redirect('/articles/%s' % art_id)

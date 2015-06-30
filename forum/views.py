from django.shortcuts import render,get_object_or_404
from .forms import QueryForm,CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import *

# Create your views here.

def home(request):
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/forum/templates/home.html')

def queries(request):

	args = {}
	args.update(csrf(request))
	
	args['queries']= Query.objects.all()

	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/forum/templates/queries.html',args)

def query(request, query_id = 1):
	return render(request, 'query.html',{'query' : Query.objects.get(id=query_id)}) 

def upvote(request,query_id, comment_id=0):
	if(comment_id==0):	
		p=get_object_or_404(Query,pk=query_id)
		p.upvotes +=1
		p.save()
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)
	elif(int(comment_id)>0):
		p=get_object_or_404(Comment,pk=comment_id)
		p.upvotes +=1
		p.save()
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)

def downvote(request,query_id,comment_id=0):
	if(comment_id==0):	
		p=get_object_or_404(Query,pk=query_id)
		p.downvotes +=1
		p.save()
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)
	elif(int(comment_id)>0):
		p=get_object_or_404(Comment,pk=comment_id)
		p.downvotes +=1
		p.save()
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)


def create(request):
	if request.POST:
		form = QueryForm(request.POST)
		# write form=QueryForm(request.POST,request.FILES) for including thumbnails
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/forum/home/queries/all')
	else:
		form = QueryForm()

	args = {}
	args.update(csrf(request))

	args['form'] = form
	
	return render(request, '/home/nikhil/Desktop/CCBT/ccbt/forum/templates/create_query.html', args)

def comment(request,query_id):
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			#form.save()
			name=form.cleaned_data['name']
			body=form.cleaned_data['body']
			pub_date=form.cleaned_data['pub_date']
			query=Query.objects.get(id=query_id)
			done=Comment.objects.create(name=name,body=body,pub_date=pub_date,query=query)
			return HttpResponseRedirect('/forum/home/queries/%s' % query_id)
	else:
		form = CommentForm()
	args = {}
	args['form'] = form
	args['query'] = Query.objects.get(id=query_id)
	return render(request, '/home/nikhil/Desktop/CCBT/ccbt/forum/templates/comment.html',args)


"""
def search_titles(request):
	if request.method=="POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''

	queries = Query.objects.filter(title__contains=search_text)

	return render(request,'ajax_search.html',{'queries':queries})
"""
















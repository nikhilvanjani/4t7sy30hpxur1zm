from django.conf.urls import url
#from forum import views
#from forum.api import QueryResource

#query_resource = QueryResource()

urlpatterns = [
	url(r'^home/$','forum.views.home',name='home'),
	url(r'^home/create/$','forum.views.create',name='create'),
	url(r'^home/queries/all/$','forum.views.queries',name='queries'),
	url(r'^home/queries/(?P<query_id>[0-9]+)/$','forum.views.query',name='query'),
	url(r'^home/queries/upvote/(?P<query_id>[0-9]+)/$','forum.views.upvote',name='upvote'),
	url(r'^home/queries/downvote/(?P<query_id>[0-9]+)/$','forum.views.downvote',name='downvote'),
	url(r'^home/queries/add_comment/(?P<query_id>[0-9]+)/$','forum.views.comment',name='comment'),
	url(r'^home/queries/upvotes/(?P<query_id>[0-9]+)/(?P<comment_id>[0-9]+)/$','forum.views.upvote',name='upvote'),
	url(r'^home/queries/downvotes/(?P<query_id>[0-9]+)/(?P<comment_id>[0-9]+)/$','forum.views.downvote',name='downvote'),
	url(r'^home/notifications/$','forum.views.notifications',name='notifications'),
	url(r'^home/latest/$','forum.views.latest',name='latest'),
	#url(r'^home/queries/search/$',views.search_titles,name='search'),
	#url(r'^api/',include(query_resource.urls)),		
]


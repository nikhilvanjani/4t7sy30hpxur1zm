from django import forms
from .models import Query,Comment

class QueryForm(forms.ModelForm):

	class Meta:
		model = Query
		fields = ('title','details','pub_date')
		#write fields = ('title','details','pub_date','thumbnail') to include thumbnails
		
class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('name','body','pub_date')

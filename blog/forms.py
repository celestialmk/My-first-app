from django import forms
from .models import Post

#creating a form with parameters title and text
class PostForm(forms.ModelForm):
     
     class Meta:
         model = Post
         fields = ('title', 'text',)
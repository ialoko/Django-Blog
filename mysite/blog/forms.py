from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control",'style': 'width: 300px;'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control",'style': 'width: 300px;'}))
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        
from django import forms
from .models import Post, Tag, Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'category', 'tags', 'is_pinned']
        widgets = {
            'contenido': TinyMCE(),
        }

class AuthorPostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'tags'] # Excluimos 'category' y 'is_pinned'
        widgets = {
            'contenido': TinyMCE(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'text',)
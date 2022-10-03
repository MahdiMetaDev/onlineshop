from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Comment
        fields = ['body', 'stars', ]
        error_messages = {'name': {'required': 'cannot be blank or null'}}

from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 10, 'placeholder': 'What is on your mind?'}
        ), 
        max_length=4000,
        help_text='Max length 4000 Characters.'
        )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
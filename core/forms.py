from django import forms
from core.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'body',
            
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'answer'
            
        ]
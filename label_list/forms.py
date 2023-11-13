from django import forms
from .models import Review
from captcha.fields import ReCaptchaField

class ReviewForm(forms.ModelForm):
    reviewer_name = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()
    
    class Meta:
        model = Review
        fields = ['reviewer_name', 'text']

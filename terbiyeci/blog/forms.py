from django import forms
from django.contrib.auth import get_user_model
from django.forms import HiddenInput

from blog.models import ShortNews
from django.contrib.auth.forms import UserCreationForm, UsernameField


class CategoriedNewsForm(forms.ModelForm):
    class Meta:
        model = ShortNews
        exclude = [
            "id",
            "score",
            "report_count",
            "parent_news",
        ]
        widgets = {
            "categories" : HiddenInput()
        }

class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":2}))

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

from django import forms
from django.forms import HiddenInput

from blog.models import ShortNews


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


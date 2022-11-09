from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms


class ArticleContentForm(forms.Form):
    content = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
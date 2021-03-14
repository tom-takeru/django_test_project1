from django.forms import ModelForm

from .models import Memo


class MemoCreateForm(ModelForm):
    class Meta:
        model = Memo
        fields = ('title', 'content', 'tags')


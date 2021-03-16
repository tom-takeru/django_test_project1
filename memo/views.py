from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import View
from django.urls import reverse_lazy, reverse

from django.http import HttpResponse, HttpResponseRedirect

import logging
logger = logging.getLogger(__name__)


from django.shortcuts import render, redirect

from .models import Memo, Tag
from .forms import MemoCreateForm

class MemoListView(ListView):
    model = Memo
    template_name = 'memo_list.html'

    def get_queryset(self):
        memo_list = Memo.objects.all().order_by('-created_at')
        return memo_list

class MemoCreateView(View):

    def get(self, request, *args, **kwargs):
        tag_list = Tag.objects.all()
        context = {
            'tag_list': tag_list,
        }
        return render(request, 'memo_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.POST["title"] != "":
            memo = Memo(title=request.POST['title'], content=request.POST['content'])
            memo.save()
            for tag in request.POST.getlist('tags'):
                memo.tags.add(tag)
        return redirect(reverse('memo:memo_list'))


# タグのアップデート
def update_add_tag(request):
    if request.POST["tag_name"] != "":
        name = Tag.objects.filter(name=request.POST["tag_name"])
        if len(name) == 0:
            tag = Tag(name=request.POST["tag_name"])
            tag.save()
    return HttpResponseRedirect(reverse('memo:memo_create'))

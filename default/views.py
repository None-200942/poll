from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView,CreateView,UpdateView,DeleteView
from .models import *
## Create your views here.
## 投票主題列表
class PollList(CreateView):
    model = Poll
    fields = ['subject','desc']
    success_url = '/poll/'
class PollList(UpdateView):
    model = Poll
    fields = ['subject','desc']
    success_url = '/poll/'
class PollList(ListView):
    model = Poll
class PollDetail(DetailView):
    model = Poll
    # 取得額外資料供頁面範本顯示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context
class PollVote(RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        opt = option.object.get(id = self.kwargs['oid'])
        opt +=1
        opr.save()
        return '/poll{}/'.format(opt.poll_id)
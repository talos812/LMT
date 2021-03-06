#-*- coding:utf-8
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import UpdateView
from CMF.models import Organization, MoneyUser, Request
from django.db.models import Q
from django.views.generic.simple import direct_to_template
from CMF.forms import RequestForm,AcceptForm
import datetime

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return direct_to_template(request, template="registration/logout.html")

class MoneyList(ListView):
    model = MoneyUser
    context_object_name = "money_list"
    template_name = "CMF/money_list.html"

    def get_context_data(self, **kwargs):
        money = MoneyUser.objects.get(owner=self.request.user)
        data = super(MoneyList, self).get_context_data(**kwargs)
        data.update({
            'user':self.request.user,
            'money': money,
        })
        return data 
class MoneyDetail(DetailView):
    model = MoneyUser
    context_object_name = "money_object"
    template_name = 'CMF/money_detail.html'
    
    def get_context_data(self, **kwargs):
        money = MoneyUser.objects.get(owner=self.request.user)
        data = super(MoneyDetail, self).get_context_data(**kwargs)
        data.update({
            'user':self.request.user,
            'money': money,
        })
        return data 
class Home(TemplateView):
    template_name = 'CMF/home.html'
    def get_context_data(self, **kwargs):
        money = MoneyUser.objects.get(owner=self.request.user)
        data = super(Home, self).get_context_data(**kwargs)
        data.update({
            'user':self.request.user,
            'money': money,
        })
        return data
    
class RequestDetail(UpdateView):
    model = Request
    form_class = AcceptForm
    context_object_name = "request"
    template_name = "CMF/request_detail.html"
    success_url = "/cmf/accept_suc/"
    
    def get_context_data(self, **kwargs):
        money = MoneyUser.objects.get(owner=self.request.user)
        data = super(RequestDetail, self).get_context_data(**kwargs)
        data.update({
            'user':self.request.user,
            'money': money,
        })
        return data 
    def get_success_url(self):
        url = super(RequestDetail, self).get_success_url()
        request = self.get_object()
        if request.is_accept:
            money_from = MoneyUser.objects.get(owner=request.from_user)
            money_to   = MoneyUser.objects.get(owner=request.to_user)
            money_from.money -= request.money
            money_to.money   += request.money
            money_from.save()
            money_to.save()            
        
        return url
        
class History(ListView):
    model = Request
    context_object_name = "request_list"
    template_name = "CMF/request_list.html"
    def get_queryset(self):
#历史只列出与自己有关的入账记录
        request_list = Request.objects.filter(
                                              Q(to_user = self.request.user) | 
                                              Q(from_user = self.request.user) ).filter(
                                              is_accept = True )
        return request_list
    def get_context_data(self, **kwargs):
        money = MoneyUser.objects.get(owner=self.request.user)
        data = super(History, self).get_context_data(**kwargs)
        data.update({
            'user':self.request.user,
            'money': money,
        })
        return data 
class MakeRequest(CreateView):
    initial = {"is_accept":False}
    model = Request
    form_class = RequestForm
    template_name = "CMF/submit_request.html"
    success_url = "/cmf/home/"
    
    def get_context_data(self, **kwargs):
        money = MoneyUser.objects.get(owner=self.request.user)
        data = super(MakeRequest, self).get_context_data(**kwargs)
        data.update({
            'user':self.request.user,
            'money': money,
        })
        return data 
class BeAcceptList(ListView):
    model = Request
    context_object_name = "request_list"
    template_name = "CMF/request_list.html"
    def get_queryset(self):
        request_list = Request.objects.filter(from_user= self.request.user).filter(is_accept=False)
        return request_list
    
    def get_context_data(self, **kwargs):
        money = MoneyUser.objects.get(owner=self.request.user)
        data = super(BeAcceptList, self).get_context_data(**kwargs)
        data.update({
            'user':self.request.user,
            'money': money,
        })
        return data 
    
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from CMF.models import Organization, MoneyUser, Request
from CMF.forms import RequestForm
import datetime
class MoneyDetail(DetailView):
    model = MoneyUser
    context_object_name = "money_object"
    template_name = 'CMF/money_detail.html'
    
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
    
class RequestDetail(DetailView):
    model = Request
    context_object_name = "request"
    template_name = "CMF/request_detail.html"
    
class History(ListView):
    model = Request
    context_object_name = "request_list"
    template_name = "CMF/request_list.html"

class MakeRequest(CreateView):
    initial = {"is_accept":False}
    model = Request
    form_class = RequestForm
    template_name = "CMF/submit_request.html"
    success_url = "/cmf/home/"
class BeAcceptList(ListView):
    model = Request
    context_object_name = "request_list"
    template_name = "CMF/request_list.html"
    def get_queryset(self):
        request_list = Request.objects.filter(to_user= self.request.user)
        return request_list
# Create your views here.
from django.views.generic import ListView, DetailView
from models import Organization, MoneyUser, Request


class MoneyDetail(DetailView):
    model = MoneyUser
    context_object_name = "money_object"
    template_name = 'CMF/money_detail.html'
    
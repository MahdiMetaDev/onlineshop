from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext as _


class HomePageView(TemplateView):
    template_name = 'home.html'


# class AboutUsPageView(TemplateView):
#     template_name = 'pages/aboutus.html'

def about_us_view(request):
    messages.error(request, _('Not built yet!'))
    return render(request, 'pages/aboutus.html')


def call_us_view(request):
    messages.error(request, _('Not built yet!'))
    return render(request, 'pages/callus.html')

from django.shortcuts import render
from django.utils.translation import gettext, get_language , activate, gettext as _

from dummypro2.settings import LANGUAGES

# Create your views here.

def home(request):
  trans = _("hello")
  return render(request, "home.html", context={"trans" : trans})

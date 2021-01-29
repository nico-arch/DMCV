from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def profile_test(request):
    return render(request, 'profile/index.html')


from django.contrib.auth.mixins import LoginRequiredMixin


class profileListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Diagnostic
    template_name = 'profile/index.html'

    #paginate_by = 10

    def get_queryset(self):
        return Diagnostic.objects.filter(dossier.utilsateur=self.request.user)

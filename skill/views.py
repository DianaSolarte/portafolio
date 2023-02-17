from django.shortcuts import render
from .models import Ability


def render_abilitys(request):
    abilitys = Ability.objects.all()
    return render(request, 'ability.html', {'abilitys': abilitys })

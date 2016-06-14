from django.shortcuts import render
from calc.forms import CalcForm
# Create your views here.


def index_view(request):
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            if form.operator == '+':
                result = form.num1 + form.num2
                return result
    return render(request, 'index.html', {"form": CalcForm()})

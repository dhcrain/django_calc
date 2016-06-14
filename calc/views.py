from django.shortcuts import render
from calc.forms import CalcForm
# Create your views here.


def index_view(request):
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['operator'])
            # if form.cleaned_data['operator'] == '+':
            result = form.cleaned_data['num1'], form.cleaned_data['operator'], form.cleaned_data['num2']
            return render(request, 'index.html', {"form": CalcForm(), 'result': result})
    return render(request, 'index.html', {"form": CalcForm()})

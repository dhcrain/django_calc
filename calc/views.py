from django.shortcuts import render
from calc.forms import CalcForm
# Create your views here.


def index_view(request):
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operator = form.cleaned_data['operator']
            print(num1, operator, num2)
            if operator == '+':
                result = num1 + num2
                next_math = CalcForm(initial={"num1": result})
                return render(request, 'index.html',
                              {"form": CalcForm(),
                               'result': result,
                               'equation': [num1, operator, num2],
                               'next_math': next_math})
            elif operator == '-':
                result = num1 - num2
                return render(request, 'index.html',
                              {"form": CalcForm(),
                               'result': result,
                               'equation': [num1, operator, num2]})
            elif operator == '/':
                result = num1 / num2
                return render(request, 'index.html',
                              {"form": CalcForm(),
                               'result': result,
                               'equation': [num1, operator, num2]})
            elif operator == '*':
                result = num1 * num2
                return render(request, 'index.html',
                              {"form": CalcForm(),
                               'result': result,
                               'equation': [num1, 'X', num2]})
    return render(request, 'index.html', {"form": CalcForm()})

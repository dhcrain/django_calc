from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from calc.forms import CalcForm
# Create your views here.


def index_view(request):
    result = 0
    num1 = 0
    num2 = 0
    operator = ""
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operator = form.cleaned_data['operator']
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '/':
                result = num1 / num2
            elif operator == 'X':
                result = num1 * num2
    next_math = CalcForm(initial={"num1": result})
    return render(request, 'index.html',
                  {"form": CalcForm(),
                   'result': result,
                   'num1': num1,
                   'num2': num2,
                   'operator': operator,
                   'next_math': next_math
                   })
    # return render(request, 'index.html', {"form": CalcForm()})


def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'user_create.html', {"form": form})
    form = UserCreationForm()
    return render(request, 'user_create.html', {"form": form})


def profile_view(request):
    return render(request, 'profile.html', {})

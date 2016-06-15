from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from calc.forms import CalcForm
from calc.models import Operation
# Create your views here.


def index_view(request):    # Calc
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
            if request.user.is_authenticated():
                Operation.objects.create(num1=num1, operator=operator, num2=num2, result=result, user=User.objects.get(id=request.user.id))
    next_math = CalcForm(initial={"num1": result})
    return render(request, 'index.html',
                  {"form": CalcForm(),
                   'result': result,
                   'num1': num1,
                   'num2': num2,
                   'operator': operator,
                   'next_math': next_math
                   })


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


@login_required
def profile_view(request):
    print(request.user)
    operations = Operation.objects.filter(user=User.objects.get(id=request.user.id))
    return render(request, 'profile.html', {"operations": operations})

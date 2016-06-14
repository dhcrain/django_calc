from django import forms


class CalcForm(forms.Form):
    operator_choice = [('+', '+'), ('-', '-'), ('/', '/'), ('*', 'X')]
    num1 = forms.FloatField()
    operator = forms.ChoiceField(operator_choice)
    num2 = forms.FloatField()

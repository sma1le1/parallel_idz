from django.shortcuts import render

def rules(request):
    return render(request, 'rules/rules.html', {})
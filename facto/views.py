
from django.shortcuts import render, HttpResponse
import re
# Create your views here.

def home(request):
    return render(request,'home.html')

def facto(request):
    value = request.POST['num']
    res = 1
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,;]')
    value = "".join(value.split())
    if value == '':
        res='Please enter a number and try again.'
        
    elif regex.search(value) != None:
        res='You have entered a Special Character. Please enter a number in input field and try again.'

    elif value.isalpha():
        res='You have entered a Character. Please enter a number in input field and try again.'

    elif int(value) < 0:
        res='You have entered a Negative value. Factorial do not exist for negative values.'
    
    else:
        for i in range(1, int(value)+1):
                    res = res*i
    
    return render(request, 'result.html', {'result':res})
        


    
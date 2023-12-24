from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('blog/index.html')
    data = {'prenom' : 'coni', 
            'montres' : ['rolex', 'tissot', 'seiko', 'casio'],
            'age' : 38,}

    return HttpResponse(template.render(data, request))
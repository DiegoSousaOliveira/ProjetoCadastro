from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def  home(request):
    return render(request, 'app1/home.html')

def index(resquest):
    nova_pessoa = Pessoa()
    nova_pessoa.nome = resquest.POST.get('nome')
    nova_pessoa.idade = resquest.POST.get('idade')
    nova_pessoa.cpf = resquest.POST.get('cpf')
    nova_pessoa.sexo = resquest.POST.get('sexo')
    nova_pessoa.save()

    lista_cadastro = {
        'lista_pessoa': Pessoa.objects.all()
    } 

    return render(resquest, 'app1/index.html', lista_cadastro)

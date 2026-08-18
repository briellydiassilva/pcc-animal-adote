from django.contrib import messages
from django.shortcuts import redirect, render

from animais.models import Animal

from .dashboard import montar_contexto_dashboard
from .forms import ContatoForm
from .models import SolicitacaoAdocao

def home(request):
    animais_carrossel = Animal.objects.prefetch_related('fotos').order_by('nome')
    return render(
        request,
        'adocao/index.html',
        {
            'animais_carrossel': animais_carrossel,
            'total_animais': Animal.objects.count(),
            'total_adocoes': SolicitacaoAdocao.objects.filter(
                status=SolicitacaoAdocao.Status.APROVADA,
            ).count(),
        },
    )

def sobre(request):
    return render(request, 'adocao/sobre.html')


def dashboard(request):
    return render(request, 'adocao/dashboard.html', montar_contexto_dashboard())

def vacinacao(request):
    return render(request, 'adocao/vacinacao.html')

def quero_adotar(request):
    return redirect('animais:lista')

def contato(request):
    dados_iniciais = {}
    if request.user.is_authenticated:
        dados_iniciais = {
            'nome': request.user.nome_completo,
            'email': request.user.email,
            'telefone': request.user.telefone,
        }

    form = ContatoForm(request.POST or None, initial=dados_iniciais)
    if request.method == 'POST' and form.is_valid():
        contato = form.save(commit=False)
        if request.user.is_authenticated:
            contato.remetente = request.user
        contato.save()
        messages.success(
            request,
            'Mensagem registrada com sucesso e disponível para a equipe administrativa.',
        )
        return redirect('contato')

    return render(request, 'adocao/contato.html', {'form': form})

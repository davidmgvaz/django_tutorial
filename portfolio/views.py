from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .forms import ComentarioForm, ComentarioModelForm
from .models import Comentario, Projeto


def teste(request):
    return HttpResponse('Ola Mundo')


def projeto_list(request):
    projetos = Projeto.objects.all()

    context = {
        'projetos': projetos
    }

    return render(request, 'projeto_list.html', context)


class ProjetoList(ListView):
    model = Projeto
#    template_name = ''
#    context_object_name = 'projetos'


def projeto_detail(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    context = {
        'projeto': projeto
    }

    return render(request, 'projeto_detail.html', context)


class ProjetoDetail(DetailView):
    model = Projeto


def comentar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.POST:
        form = ComentarioModelForm(request.POST)

        if form.is_valid():
            comentario = Comentario(
                projeto=projeto,
                nome=form.cleaned_data['nome'],
                comentario=form.cleaned_data['comentario']
            )
            comentario.save()
    else:
        form = ComentarioModelForm()

    context = {
        "form": form,
        "projeto": projeto
    }

    return render(request, "portfolio/projeto_detail.html", context)
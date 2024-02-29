from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Filme
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme

class Pesquisafilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=pesquisa)
            return object_list
        else:
            return None

class Detalhefilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhefilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context
    
class Homecategoriaacao(ListView):
    template_name = 'homecategoriaacao.html'git 
    model = Filme
    
class Homecategoriaficcao(ListView):
    template_name = 'homecategoriaficcao.html'
    model = Filme

class Homecategoriaanimacao(ListView):
    template_name = 'homecategoriaanimacao.html'
    model = Filme

class Homecategoriasuspense(ListView):
    template_name = 'homecategoriasuspense.html'
    model = Filme

class Homecategoriadrama(ListView):
    template_name = 'homecategoriadrama.html'
    model = Filme

class Homecategoriacomedia(ListView):
    template_name = 'homecategoriacomedia.html'
    model = Filme

class Homecategoriaterror(ListView):
    template_name = 'homecategoriaterror.html'
    model = Filme

class Homecategoriadocumentario(ListView):
    template_name = 'homecategoriadocumentario.html'
    model = Filme

class Homecategoriaromance(ListView):
    template_name = 'homecategoriaromance.html'
    model = Filme




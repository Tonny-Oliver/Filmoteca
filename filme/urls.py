from django.urls import path
from .views import Homefilmes, Detalhefilme, Homecategoriaacao, Homecategoriaficcao, Homecategoriaanimacao, Homecategoriasuspense, Pesquisafilme, Homecategoriacomedia, Homecategoriadrama, Homecategoriadocumentario, Homecategoriaromance, Homecategoriaterror



app_name = 'filme'

urlpatterns = [
    # path('', Homepage.as_view(), name='homepage'),
    path('', Homefilmes.as_view(), name='homefilmes'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisa'),
    path('filmes/<int:pk>', Detalhefilme.as_view(), name='detalhefilme'),
    path('filmes/acao/', Homecategoriaacao.as_view(), name='homecategoriaacao'),
    path('filmes/ficcao/', Homecategoriaficcao.as_view(), name='homecategoriaficcao'),
    path('filmes/animacao/', Homecategoriaanimacao.as_view(), name='homecategoriaanimacao'),
    path('filmes/suspense/', Homecategoriasuspense.as_view(), name='homecategoriasuspense'),
    path('filmes/comedia/', Homecategoriacomedia.as_view(), name='homecategoriacomedia'),
    path('filmes/drama/', Homecategoriadrama.as_view(), name='homecategoriadrama'),
    path('filmes/terror/', Homecategoriaterror.as_view(), name='homecategoriaterror'),
    path('filmes/documentario/', Homecategoriadocumentario.as_view(), name='homecategoriadocumentario'),
    path('filmes/romance/', Homecategoriaromance.as_view(), name='homecategoriaromance'),
]

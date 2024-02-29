from .models import Filme

def adicionados_recentemente(request):
    # seleção de adicionados rescentemente
    recentes = Filme.objects.all().order_by('-data_criacao')[0:5]

    # seleções por categoria em ordem aleatoria 
    acao = Filme.objects.filter(categoria='acao').order_by('?')[0:5]
    animacao = Filme.objects.filter(categoria='animacao').order_by('?')[0:5]
    aventura = Filme.objects.filter(categoria='aventura').order_by('?')[0:5]
    ficcao = Filme.objects.filter(categoria='ficcao').order_by('?')[0:5]
    suspense = Filme.objects.filter(categoria='suspense').order_by('?')[0:5]
    terror = Filme.objects.filter(categoria='terror').order_by('?')[0:5]
    drama = Filme.objects.filter(categoria='drama').order_by('?')[0:5]

    # seleção de visualização
    vistos = Filme.objects.all().order_by('-visualizacao')[0:5]
    
    return {'adicionados_recentemente': recentes, 'lista_acao': acao, 'lista_animacao': animacao, 'lista_aventura': aventura, 
            'lista_ficcao': ficcao, 'lista_suspense': suspense, 'lista_terror': terror, 'vistos': vistos, 'drama': drama,
            }

def pag_filmes(request):

    pag_acao = Filme.objects.filter(categoria='acao').order_by('-data_criacao')
    pag_ficcao = Filme.objects.filter(categoria='ficcao').order_by('-data_criacao')
    pag_animacao = Filme.objects.filter(categoria='animacao').order_by('-data_criacao')
    pag_suspense = Filme.objects.filter(categoria='suspense').order_by('-data_criacao')
    pag_comedia = Filme.objects.filter(categoria='comedia').order_by('-data_criacao')
    pag_drama = Filme.objects.filter(categoria='drama').order_by('-data_criacao')
    pag_terror = Filme.objects.filter(categoria='terror').order_by('-data_criacao')
    pag_documentario = Filme.objects.filter(categoria='documentario').order_by('-data_criacao')
    pag_romance = Filme.objects.filter(categoria='romance').order_by('-data_criacao')

    return {'pag_acao': pag_acao, 'pag_ficcao': pag_ficcao, 'pag_animacao': pag_animacao, 'pag_suspense': pag_suspense, 'pag_drama': pag_drama,
            'pag_comedia': pag_comedia, 'pag_terror': pag_terror, 'pag_documentario': pag_documentario, 'pag_romance': pag_romance
            }
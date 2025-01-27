import json
from datetime import datetime
import os

ARQUIVO_DADOS = 'noticias.json'

banco = {}
contador_id = 1

def carregar_dados():
    global banco, contador_id
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            banco = dados.get('noticias', {})
            contador_id = dados.get('contador_id', 1)
    else:
        salvar_dados()

def salvar_dados():
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump({'noticias': banco, 'contador_id': contador_id}, arquivo, ensure_ascii=False, indent=4)

def formatar_autor(nome: str):
    partes = nome.split()
    if len(partes) == 1:
        return f"{partes[-1]}, {' '.join(partes[:-1])}"
    return nome

def formatar_data():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def adicionar_noticia(titulo: str, conteudo: str, autor: str):
    global contador_id
    identificador = contador_id
    contador_id += 1
    data_criacao = formatar_data()
    banco[identificador] = {
        'id': identificador,
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': formatar_autor(autor),
        'data_criacao': data_criacao,
        'removido': False,
        'data_remocao': None
    }
    salvar_dados()
    return banco[identificador]

def editar_noticia(identificador: int, titulo: str, conteudo: str, autor: str):
    if identificador not in banco:
        raise KeyError("Notícia não encontrada.")
    
    banco[identificador].update({
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': formatar_autor(autor),
        'data_criacao': formatar_data()
    })
    salvar_dados()
    return banco[identificador]

def listar_noticia(identificador: int):
    if identificador not in banco:
        raise KeyError("Notícia não encontrada.")
    return banco[identificador]

def listar_todas_noticias():
    return banco

def remover_noticia(identificador: int):
    if identificador in banco:
        banco[identificador]['removido'] = True
        banco[identificador]['data_remocao'] = formatar_data()
        salvar_dados()
    else:
        raise KeyError("Notícia não encontrada.")

def restaurar_noticia(identificador: int):
    if identificador in banco and banco[identificador]['removido']:
        banco[identificador]['removido'] = False
        banco[identificador]['data_remocao'] = None
        salvar_dados()
        return banco[identificador]
    raise KeyError("Notícia não encontrada ou não removida.")

carregar_dados()

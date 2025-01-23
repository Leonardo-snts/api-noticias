from datetime import datetime

banco = {}
contador_id = 1

def formatar_autor(nome: str):
    partes = nome.split()
    if len(partes) == 1:
        return f"{partes[-1]}, {' '.join(partes[:-1])}"
    return nome

def formatar_data():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def adicionar_noticia(
    titulo: str,
    conteudo: str,
    #publicado: bool,
    autor: str
):
    global contador_id
    identificador = contador_id
    contador_id += 1
    data_criacao = formatar_data()
    banco[identificador] = {
        'id': identificador,
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': formatar_autor(autor),
        #'publicado': publicado,
        'data_criacao': data_criacao
    }
    return banco[identificador] 

def editar_noticia(
    identificador: int,
    titulo: str,
    conteudo: str,
    #publicado: bool,
    autor: str
):
    data_criacao = formatar_data()
    banco[identificador] = {
        'id': identificador,
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': formatar_autor(autor),
        #'publicado': publicado,
        'data_criacao': data_criacao
    }
    return banco[identificador]

def listar_noticia(identificador: int):
    return banco[identificador]

def listar_todas_noticias():
    return banco

def remover_noticia(identificador: int):
    del banco[identificador]

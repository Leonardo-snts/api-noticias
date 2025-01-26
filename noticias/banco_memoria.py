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
        'data_criacao': data_criacao
    }
    return banco[identificador] 

def editar_noticia(
    identificador: int,
    titulo: str,
    conteudo: str,
    autor: str
):
    data_criacao = formatar_data()
    banco[identificador] = {
        'id': identificador,
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': formatar_autor(autor),
        'data_criacao': data_criacao
    }
    return banco[identificador]

def listar_noticia(identificador: int):
    return banco[identificador]

def listar_todas_noticias():
    return banco

def remover_noticia(identificador: int):
    if identificador in banco:
        banco[identificador]['removido'] = True
        banco[identificador]['data_remocao'] = formatar_data()
    else:
        raise KeyError("Notícia não encontrada.")

def restaurar_noticia(identificador: int):
    if identificador in banco and banco[identificador]['removido']:
        banco[identificador]['removido'] = False
        banco[identificador]['data_remocao'] = None
        return banco[identificador]
    raise KeyError("Notícia não encontrada ou não removida.")

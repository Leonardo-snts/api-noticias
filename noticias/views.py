from rest_framework import status, views
from rest_framework.response import Response
from .serializers import NoticiaSerializer
from .banco_memoria import (
    adicionar_noticia,
    editar_noticia,
    listar_noticia,
    listar_todas_noticias,
    remover_noticia,
    restaurar_noticia
)

class NoticiaListCreateView(views.APIView):
    def get(self, request):
        noticias = listar_todas_noticias().values()
        return Response(noticias, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NoticiaSerializer(data=request.data)
        if serializer.is_valid():
            noticia = adicionar_noticia(
                titulo=serializer.validated_data['titulo'],
                conteudo=serializer.validated_data['conteudo'],
                autor=serializer.validated_data['autor']
            )
            return Response(noticia, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticiaDetailView(views.APIView):
    def get(self, request, id):
        try:
            noticia = listar_noticia(id)
            return Response(noticia, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'error': 'Notícia não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            serializer = NoticiaSerializer(data=request.data)
            if serializer.is_valid():
                noticia = editar_noticia(
                    identificador=id,
                    titulo=serializer.validated_data['titulo'],
                    conteudo=serializer.validated_data['conteudo'],
                    autor=serializer.validated_data['autor']
                )
                return Response(noticia, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Notícia não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            remover_noticia(id)
            return Response({'message': 'Notícia removida com sucesso'}, status=status.HTTP_204_NO_CONTENT)
        except KeyError:
            return Response({'error': 'Notícia não encontrada'}, status=status.HTTP_404_NOT_FOUND)

class NoticiaRestaurarView(views.APIView):
    def put(self, request, id):
        try:
            noticia = restaurar_noticia(id)
            return Response({'message': 'Notícia restaurada com sucesso', 'noticia': noticia}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'error': 'Notícia não encontrada ou não removida'}, status=status.HTTP_404_NOT_FOUND)

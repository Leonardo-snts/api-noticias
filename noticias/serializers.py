from rest_framework import serializers

class NoticiaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=255)
    conteudo = serializers.CharField()
    autor = serializers.CharField()
    data_criacao = serializers.CharField(read_only=True)

    def validate_autor(self, value):
        partes = value.split()
        if len(partes) > 1:
            return f"{partes[-1]}, {' '.join(partes[:-1])}"
        return value

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Postagem import Postagem
from api.serializers import PostagemSerializer, ComentarioSerializer, UsuarioSerializer
from api.model.teste import Comentario
from django.shortcuts import get_object_or_404
from api.models import Usuario


class PostagemList(APIView):
    def get(self, request):
        postagem = Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data

        return Response(data)

    def post(self, request):
        nome = request.data['nome']
        descricao = request.data['descricao']
        postagem = Postagem(nome= nome, descricao=descricao)
        postagem.save()
        data = PostagemSerializer(postagem).data

        return Response(data)

class PostagemDetail(APIView):
    def delete(self,request,pk):
        post = get_object_or_404(Postagem, pk=pk)
        post.delete()

        data = PostagemSerializer(post).data

        return Response(data)


class ComentarioList(APIView):
    def post(self, request):
        texto_comentario = request.data['texto_do_json']
        postagem_id = request.data['postagem_id']

        post = get_object_or_404(Postagem, pk=postagem_id)

        comentar = Comentario(texto=texto_comentario, postagem=post)
        comentar.save()
        data = ComentarioSerializer(comentar).data

        return Response(data)

class ComentarioDetail(APIView):
    def get(self,request, pk):
        #/postagem/comentario/<id>
        post = get_object_or_404(Postagem, pk=pk)

        comentario = Comentario.objects.filter(postagem=post)

        data = ComentarioSerializer(comentario, many=True).data

        return Response(data)

class UsuarioList(APIView):
    def post(self, request):
        username = request.data['username'] # o que está em laranja é escrito no insomnia
        email = request.data['email']
        password = request.data['password']
        nome = request.data['nome']
        is_admin = request.data['is_admin']
        

        user = Usuario(nome=nome,email=email, username=username, is_admin=is_admin)
        user.set_password(password)
        validate = Usuario.objects.filter(username=username)
        validate_email = Usuario.objects.filter(email=email)

        if not (UsuarioSerializer(validate, many=True).data or UsuarioSerializer(validate_email, many=True).data):
            user.save()
            data = UsuarioSerializer(user).data
            return Response(data)
        else:
            return Response({'error':'User already exists'})




    #/comentario/4
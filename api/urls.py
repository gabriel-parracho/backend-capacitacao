from django.urls import path
from api.views import PostagemList, ComentarioList, ComentarioDetail, PostagemDetail, UsuarioList

urlpatterns = [
    path('postagem/', PostagemList.as_view()),
    path('postagem/comentario/', ComentarioList.as_view()),
    path('postagem/comentario/<int:pk>', ComentarioDetail.as_view()),
    path('postagem/<int:pk>', PostagemDetail.as_view()),
    path('user/', UsuarioList.as_view())
    #/postagem/comentario/1

]

from django.urls import path
from . import views

urlpatterns = [
    path('code/<str:code_id>/', views.view_code),
    path('code/<str:code_id>/<str:code_op>/', views.view_code),
    path('match/<str:match_name>/', views.view_pairmatch),
    path('match/<str:match_name>/<str:record_id>/', views.view_record),
    path('upload/', views.upload),
    path('game/<str:AI_type>/', views.game_info),
    path('lobby/', views.lobby),
    path('lobby/run_match/<str:AI_type>/', views.pairmatch),
    path('lobby/ladder/<str:AI_type>/', views.ladder),
    path('lobby/ranked_match/<str:AI_type>/', views.ranked_match),
    path('lobby/invitation/<str:AI_type>/', views.invite_match),
]

from django.urls import path

from core.views import *


urlpatterns = [
	path('<str:video_personality_doc_id>/', VideoPersonalityFetchViewWithRedisConnectionpool.as_view()),
]
from django.urls import path

from core.views import VideoPersonalityFetchView


urlpatterns = [
	path('<str:video_personality_doc_id>/', VideoPersonalityFetchView.as_view()),
]
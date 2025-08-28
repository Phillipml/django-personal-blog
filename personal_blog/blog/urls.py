from django.urls import path
from .views.post__views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
]
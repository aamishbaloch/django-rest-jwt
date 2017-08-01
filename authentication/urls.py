from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^register/', views.RegistrationView.as_view()),
    url(r'^login/', views.LoginView.as_view())
]

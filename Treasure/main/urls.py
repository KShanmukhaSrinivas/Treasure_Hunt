from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('signup', views.sigunup, name = 'signup'),
    path('puzzle1/<int:ans>', views.puzzle1, name = 'puzzle1'),
    path('puzzle2/<int:ans>', views.puzzle2, name = 'puzzle2'),
    path('puzzle3/<int:ans>', views.puzzle3, name = 'puzzle3')

]
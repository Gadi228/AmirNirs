from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('section/<slug:sec_slug>/', SectionView.as_view(), name='section'),
    path('view/<slug:view_slug>', ViewView.as_view(), name='view'),
    path('about/', About, name="about"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('records/', RecordsView.as_view(), name="record"),
    path('saveorder/', saveorder, name="saveorder"),
    path('payment/', payment, name='payment')

]


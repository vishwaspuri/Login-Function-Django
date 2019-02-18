from django.conf.urls import url
from blog import views

#template urls
app_name='blog'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.show_profile),
]
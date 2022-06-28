from django.urls import path
from . import views


#organize urls by app. makes app resuable
app_name = 'blog'

urlpatterns = [
    #post views

    #no argument and mapped to post_list view
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    #4 arguments mapped to post_detail
    #angle brackets capture value from urls
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
                            views.post_detail,
                            name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name ='post_share'),
    
]
from django.urls import path
from .views import registerapi,loginapi,deleteview

from knox import views as kv
urlpatterns=[

    path('api/register/',registerapi.as_view(),name="register"),
    path('api/login/',loginapi.as_view(),name='loign'),
    path('api/delete/',deleteview.as_view(),name='delete'),
    # path('api/login/',loginapi.as_view(),name='login'),
    # path('api/logout/',kv.LogoutView.as_view(),'logout'),
    # path('api/logoutall/',kv.LogoutAllView.as_view(),'logoutall'),
]

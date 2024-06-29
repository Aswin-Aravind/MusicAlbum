from django.urls import path

from rest_framework.routers import DefaultRouter

from api.views import AlbumViewSetViews,TrackMixinView,UserRegisterView,UserActivityView

from rest_framework.authtoken.views import ObtainAuthToken



router = DefaultRouter()

router.register('albums',AlbumViewSetViews,basename='albums')

router.register('userregister',UserRegisterView,basename="user_register")

router.register("userreview",UserActivityView,basename="userreview")


urlpatterns = [

    path('token/',ObtainAuthToken.as_view()),
    path('tracks/<int:pk>/',TrackMixinView.as_view()),


    
]+router.urls
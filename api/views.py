from django.shortcuts import render

from django.contrib.auth.models import User

from api.serializers import AlbumSerializer,TrackSerializer,UserSerializer,ReviewSerializer

from api.models import Album,Track,Review

from rest_framework.viewsets import ModelViewSet,ViewSet

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.response import Response

from rest_framework.decorators import action

from rest_framework import authentication,permissions

from rest_framework import serializers





class UserRegisterView(ViewSet):

    def create(self,request,*args,**kwargs):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        


class UserActivityView(ViewSet):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]
    # url":lh:8000/activity/{a.id}/
    
    
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        album_instance = Album.objects.get(id=id)

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user,album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        

    

    def list(self,request,*args,**kwargs):

        qs=Album.objects.all()

        serializer = AlbumSerializer(qs,many=True)

        return Response(data=serializer.data)
    


    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        qs = Review.objects.get(id=id)

        if qs.user==request.user:

            serializer = ReviewSerializer(qs)

            return Response(data=serializer.data)
        
        else:

            raise serializers.ValidationError("not allowed")
        


    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs = Review.objects.get(id=id)

        serializer = ReviewSerializer(data=request.data,instance=qs)

        if serializer.is_valid():

            if qs.user==request.user:

              serializer.save()

              return Response(data=serializer.data)
            
        else:

            return Response(data=serializer.errors)
        

    

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        qs=Review.objects.get(id=id)

        if qs.user==request.user:

            qs.delete()

            return Response({"message":"successfully deleted."})
        
        else:

            return Response({"message":"error occured"})
        
    

        



class AlbumViewSetViews(ModelViewSet):

    serializer_class = AlbumSerializer

    queryset = Album.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]
    

    @action(methods=["post"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id = kwargs.get('pk')

        album_instance = Album.objects.get(id=id)

        serializer = TrackSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album = album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        


class TrackMixinView(RetrieveUpdateDestroyAPIView):

    serializer_class = TrackSerializer

    queryset = Track.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    

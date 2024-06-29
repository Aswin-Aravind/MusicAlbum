from rest_framework import serializers


from api.models import Album,Track,Review

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","password","email","first_name","last_name"]

        read_only_fields = ["id"]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data) 


class TrackSerializer(serializers.ModelSerializer):

    album = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Track

        fields = "__all__"

        read_only_fields = ["id","album"]



class ReviewSerializer(serializers.ModelSerializer):

    album = serializers.StringRelatedField(read_only=True)

    user = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Review

        fields = "__all__"

        read_only_fields = ["id","user","album"]




class AlbumSerializer(serializers.ModelSerializer):

    track_count = serializers.CharField(read_only=True)

    tracks = TrackSerializer(many=True,read_only=True)

    review = ReviewSerializer(many=True,read_only=True)

    # comment = ReviewSerializer(many=True,read_only=True)

    class Meta:

        model = Album

        fields = "__all__"

        read_only_fields = ["id","is_active"]






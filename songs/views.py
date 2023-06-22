from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset=Song.objects.all()
    serializer_class = SongSerializer
    lookup_url_kwarg="pk"


    # def get(self, request, pk):

    #     songs = Song.objects.filter(album_id=pk)

    #     result_page = self.paginate_queryset(songs, request)
    #     serializer = SongSerializer(result_page, many=True)

    #     return self.get_paginated_response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("pk"))

        # album = get_object_or_404(Album, pk=pk)

        # serializer = SongSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save(album=album)

        # return Response(serializer.data, status.HTTP_201_CREATED)

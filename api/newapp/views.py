from django.shortcuts import render
from jet.filters import RelatedFieldAjaxListFilter
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework import status
from rest_framework.permissions import  IsAdminUser
from newapp.permissions import  Is_authenticated

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email','name')
    def activate_account(request, hash):
        user = authenticate(hash=hash)
        if user:
            login(request, user)
        else:
            return user_not_found_bad_hash_message

class IncidentsViewSet(viewsets.ModelViewSet):
    #permission_classes = (Is_authenticated,)
    serializer_class = serializers.IncidentsSerializer
    queryset = models.Incidents.objects.all()

class DetailViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DetailSerializer
    queryset = models.Detail.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('frequence','commentaire','userId','motivation')

    # def create(self, request, *args, **kwargs):
    #     is_many = isinstance(request.data, list)
    #     if not is_many:
    #         return super(DetailViewSet, self).create(request, *args, **kwargs)
    #     else:
    #         serializer = self.get_serializer(data=request.data, many=True)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TransportsViewSet(viewsets.ModelViewSet): 
    serializer_class = serializers.TransportsSerializer
    queryset = models.Transports.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nom')

class TypeIncidentsViewSet(viewsets.ModelViewSet): 
    serializer_class = serializers.TypeIncidentsSerializer
    queryset = models.TypeIncidents.objects.all()

class MotivationViewSet(viewsets.ModelViewSet): 
    serializer_class = serializers.MotivationSerializer
    queryset = models.Motivation.objects.all()


class PeriodeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PeriodeSerializer
    queryset = models.Periode.objects.all().order_by('-date')
    filter_backends = (filters.SearchFilter,)
    search_fields = ("annee", "commentaire")


class GroupViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAdminUser,)
    serializer_class = serializers.GroupSerializer
    queryset = models.Group.objects.all()
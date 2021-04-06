from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.models import User, Group

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, ContactSerializer, ReservationSerializer, MenuSerializer
from .models import Contact, Reservation, Menu


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


#contact
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ContactList(APIView):
    # # JSON loaded/parsed data
    # data = json.loads(request.body)
    def get(self, request, format=None):
        contacts = Contact.objects.all().order_by('-createdDate')
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetail(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contacts = self.get_object(pk)
        serializer = ContactSerializer(contacts)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contacts = self.get_object(pk)
        serializer = ContactSerializer(contacts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contacts = self.get_object(pk)
        contacts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#reservation
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ReservationList(APIView):
    # # JSON loaded/parsed data
    # data = json.loads(request.body)
    def get(self, request, format=None):
        reservations = Reservation.objects.all().order_by('-createdDate')
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationDetail(APIView):
    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reservations = self.get_object(pk)
        serializer = ReservationSerializer(reservations)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reservations = self.get_object(pk)
        serializer = ReservationSerializer(reservations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservations = self.get_object(pk)
        reservations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#menu
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MenuList(APIView):
    # # JSON loaded/parsed data
    # data = json.loads(request.body)
    def get(self, request, format=None):
        menus = Menu.objects.all().order_by('-createdDate')
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetail(APIView):
    def get_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        menus = self.get_object(pk)
        serializer = MenuSerializer(menus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        menus = self.get_object(pk)
        serializer = MenuSerializer(menus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        menus = self.get_object(pk)
        menus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

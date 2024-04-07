from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer


# Create your views here.

def index(request):
     return render(request, 'index.html', {})

def home(request):
    return render(request, 'home.html')

class MenuItemView(ListCreateAPIView):
     queryset = Menu.objects.all()
     serializer_class = menuSerializer

     def get(self, request):
          items = self.get_queryset()
          serialzer = menuSerializer(items, many = True)
          return Response(serialzer.data)

     def post(self, request):
          serialzer = menuSerializer(data = request.data)
          if serialzer.is_valid():
               serialzer.save()
               return Response(serialzer.data, status=status.HTTP_201_CREATED)
          return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
     queryset = Menu.objects.all()
     serializer_class = menuSerializer

     def get(self, request, pk):
          item = self.get_queryset().get(pk=pk)
          serialzer = menuSerializer(item)
          return Response(serialzer.data)

     def post(self, request, pk):
          item = self.queryset().get(pk=pk)
          serialzer = menuSerializer(item, data = request.data)
          if serialzer.is_valid():
               serialzer.save()
               return Response(serialzer.data, status=status.HTTP_201_CREATED)
          return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
          try:
               item = self.queryset().get(pk=pk)
               item.delete()
               return Response(status=status.HTTP_204_NO_CONTENT)
          except Menu.DoesNotExist:
               return Response(status=status.HTTP_404_NOT_FOUND)

class BookingViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticated]

     queryset = Booking.objects.all()
     serializer_class = bookingSerializer
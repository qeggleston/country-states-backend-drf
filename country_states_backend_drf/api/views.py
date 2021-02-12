from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Country, State
from .serializers import CountrySerializer, StateSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status

# Create your views here.
class CountryList(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StateList(APIView):
    def get(self, request, format=None):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateListByCountry(APIView):
    def get(self, request, code, format=None):
        country = Country.objects.get(code=code)
        states = State.objects.filter(country=country)
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass
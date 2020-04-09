from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from api.models import Weekday, Campaign
from api.serializers import WeekdaySerializer, CampaignSerializer
import stripe

class WeekdayList(APIView):
    '''Get all categories or create a category'''
    @csrf_exempt
    def get(self, request, format=None):
        cats = Weekday.objects.all()
        if request.query_params.get('day'):
            cats = cats.filter(title__contains=request.query_params.get('day'))
        serializer = WeekdaySerializer(cats, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = WeekdaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeekdayDetail(APIView):
    '''Work with an individual Category object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        cat = Weekday.objects.get(id=pk)
        serializer = WeekdaySerializer(cat)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        cat = Weekday.objects.get(id=pk)
        serializer = WeekdaySerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        cat = Weekday.objects.get(id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CampaignList(APIView):
    '''Get all categories or create a category'''
    @csrf_exempt
    def get(self, request, format=None):
        cats = Campaign.objects.all()
        if request.query_params.get('url'):
            cats = cats.filter(title__contains=request.query_params.get('url'))
        elif request.query_params.get('campaign_id'):
            cats = cats.filter(title__contains=request.query_params.get('campaign_id'))
        elif request.query_params.get('auto_fb_post_mode'):
            cats = cats.filter(title__contains=request.query_params.get('auto_fb_post_mode'))
        elif request.query_params.get('current_amount'):
            cats = cats.filter(title__contains=request.query_params.get('current_amount'))
        elif request.query_params.get('goal'):
            cats = cats.filter(title__contains=request.query_params.get('goal'))
        elif request.query_params.get('donators'):
            cats = cats.filter(title__contains=request.query_params.get('donators'))
        elif request.query_params.get('days_active'):
            cats = cats.filter(title__contains=request.query_params.get('days_active'))
        elif request.query_params.get('title'):
            cats = cats.filter(title__contains=request.query_params.get('title'))
        elif request.query_params.get('description'):
            cats = cats.filter(title__contains=request.query_params.get('description'))
        elif request.query_params.get('price'):
            cats = cats.filter(title__contains=request.query_params.get('price'))
        serializer = CampaignSerializer(cats, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CampaignDetail(APIView):
    '''Work with an individual Category object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        cat = Campaign.objects.get(id=pk)
        serializer = CampaignSerializer(cat)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        cat = Campaign.objects.get(id=pk)
        serializer = CampaignSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        cat = Campaign.objects.get(id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



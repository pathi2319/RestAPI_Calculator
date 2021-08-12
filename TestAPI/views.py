from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.

@api_view(["GET"])
def add(request):
    try:
        values=json.loads(request.body)
        print("Here")
        print(values)
        values1=json.dumps(values)
        print(values1)
        print(values['c'])
        if values['c']=='add':
            result=values['a']+values['b']
        elif values['c']=='sub':
            result=values['a']-values['b']
        else :
            result=values['a']*values['b']
        # a=0
        # for key in values:
        #
        #     result=a+values[key]
        #     a = result
        return JsonResponse(result,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
@api_view(["PUT"])
def subtract(request):
    try:
        values=json.loads(request.body)
        values1=json.dumps(values)
        print(values1)
        return JsonResponse(values.get("a")+values.get("b"),safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def multiple(request):
    try:
        values=json.loads(request.body)
        # print("Here")
        # print(values)
        # values1=json.dumps(values)
        # print(values1)

        return JsonResponse(values.get("a")+values.get("b"),safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
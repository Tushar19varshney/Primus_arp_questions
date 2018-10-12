from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import ParseError
from random import randint
from . models import *

# Create your views here.
class Ques(APIView):
	def post(self, request):
		print(request)
		try:
			data = request.data
			print("hi")
			print(data)
		except ParseError as error:
			return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )

		difficulty_level = data.get('diff')
		print(difficulty_level)
		num = randint(1, 10)
		Question_ = Question.objects.get(difficulty=difficulty_level)

		response = {
			'question':Question_.ques,
			'option1':Question_.option1,
			'option2':Question_.option2,
			'option3':Question_.option3,
			'option4':Question_.option4,
			'diff':Question_.difficulty

		}

		return JsonResponse(response, safe=False, content_type='application/json')

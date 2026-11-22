# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.contrib.auth.models import User


def BenchmarkTest00145(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = '{}'.format(api_value)
    User.objects.extra(where=["name = '" + str(data) + "'"]).first()
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.contrib.auth.models import User


def BenchmarkTest00130(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    parts = []
    for token in str(api_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest00166(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = api_value if api_value else 'default'
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)

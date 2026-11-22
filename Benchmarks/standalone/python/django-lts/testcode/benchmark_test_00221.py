# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.contrib.auth.models import User


def BenchmarkTest00221(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    def normalize(value):
        return value.strip()
    data = normalize(api_value)
    matches = len(User.objects.raw("SELECT * FROM users WHERE name = '" + str(data) + "'"))
    return JsonResponse({'matches': matches}, status=200)

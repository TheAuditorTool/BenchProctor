# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest00050(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    parts = []
    for token in str(api_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return JsonResponse({"saved": True})

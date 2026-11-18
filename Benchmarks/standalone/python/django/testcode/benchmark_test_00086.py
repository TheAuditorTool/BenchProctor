# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest00086(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = '%s' % str(api_value)
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return JsonResponse({"saved": True})

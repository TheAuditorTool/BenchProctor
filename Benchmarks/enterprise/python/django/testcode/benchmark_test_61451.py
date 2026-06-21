# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest61451(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    requests.post('https://api.prod.internal/data', data=str(profile_value), verify=True)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest76308(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = f'{profile_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

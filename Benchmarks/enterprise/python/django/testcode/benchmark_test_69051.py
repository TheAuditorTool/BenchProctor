# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest69051(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = (lambda v: v.strip())(profile_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

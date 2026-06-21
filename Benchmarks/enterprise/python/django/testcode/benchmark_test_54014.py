# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest54014(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = FormData(payload=profile_value).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})

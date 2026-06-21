# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest41388(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    kind = 'json' if str(profile_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = profile_value
            data = parsed
        case _:
            data = profile_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

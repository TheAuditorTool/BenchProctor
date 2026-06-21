# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import urllib.request
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest76432(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})

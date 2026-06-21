# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest02631(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get(str(processed))
    return JsonResponse({"saved": True})

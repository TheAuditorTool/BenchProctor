# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest69935(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get(str(processed))
    return JsonResponse({"saved": True})

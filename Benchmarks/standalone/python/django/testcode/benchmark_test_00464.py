# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00464(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    form = FormData(payload=comment_value)
    data = form.payload
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return JsonResponse({'error': 'not found'}, status=404)
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)

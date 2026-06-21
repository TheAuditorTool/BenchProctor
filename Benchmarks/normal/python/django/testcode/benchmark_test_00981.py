# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest00981(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ensure_str(origin_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return JsonResponse({'record': str(record)}, status=200)

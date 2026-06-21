# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import re
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest03530(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00451(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    form = FormData(payload=comment_value)
    data = form.payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)

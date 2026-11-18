# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00683(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    form = FormData(payload=db_value)
    data = form.payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)

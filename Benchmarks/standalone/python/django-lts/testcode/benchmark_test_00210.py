# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00210(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    form = FormData(payload=origin_value)
    data = form.payload
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)

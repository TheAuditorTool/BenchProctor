# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00023(request):
    cookie_value = request.COOKIES.get('session_token', '')
    form = FormData(payload=cookie_value)
    data = form.payload
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)

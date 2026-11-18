# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00276(request, path_param):
    path_value = path_param
    form = FormData(payload=path_value)
    data = form.payload
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)

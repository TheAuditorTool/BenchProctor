# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest65260(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)

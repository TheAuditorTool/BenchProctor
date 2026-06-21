# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest65272(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = FormData(payload=ua_value).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)

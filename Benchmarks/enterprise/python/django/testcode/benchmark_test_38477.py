# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest38477(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)

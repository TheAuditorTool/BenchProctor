# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest02385(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest61015(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

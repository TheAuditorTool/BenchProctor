# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest55135(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

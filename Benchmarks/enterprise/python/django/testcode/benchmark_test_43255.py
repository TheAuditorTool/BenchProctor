# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest43255(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)

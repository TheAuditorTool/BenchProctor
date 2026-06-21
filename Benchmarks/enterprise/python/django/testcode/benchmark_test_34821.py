# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest34821(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})

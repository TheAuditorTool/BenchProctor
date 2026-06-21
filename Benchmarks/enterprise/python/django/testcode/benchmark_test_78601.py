# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest78601(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = FormData(payload=ua_value).payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})

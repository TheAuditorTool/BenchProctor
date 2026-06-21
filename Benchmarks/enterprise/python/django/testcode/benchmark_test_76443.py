# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest76443(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = FormData(payload=forwarded_ip).payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest14915(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = FormData(payload=referer_value).payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest20610(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest05376(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

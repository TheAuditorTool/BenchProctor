# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest64836(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

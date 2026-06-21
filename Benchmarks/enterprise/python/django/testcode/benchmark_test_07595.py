# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest07595(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

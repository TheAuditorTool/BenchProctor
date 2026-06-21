# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest02197(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)

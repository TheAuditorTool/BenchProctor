# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest30307(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})

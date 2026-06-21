# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest59891(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)

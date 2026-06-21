# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest08802(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)

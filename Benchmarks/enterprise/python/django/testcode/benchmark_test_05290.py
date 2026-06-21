# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest05290(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

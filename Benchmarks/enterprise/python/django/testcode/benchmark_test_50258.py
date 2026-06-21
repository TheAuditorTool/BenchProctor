# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest50258(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    requests.get(str(data))
    return JsonResponse({"saved": True})

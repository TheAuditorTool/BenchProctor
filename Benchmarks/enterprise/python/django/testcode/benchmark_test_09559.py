# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import urllib.request


@dataclass
class FormData:
    payload: str

def BenchmarkTest09559(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})

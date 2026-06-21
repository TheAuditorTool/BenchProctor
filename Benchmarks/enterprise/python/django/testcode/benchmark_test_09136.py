# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest09136(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})

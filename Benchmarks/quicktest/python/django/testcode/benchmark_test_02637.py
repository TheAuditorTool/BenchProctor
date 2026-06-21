# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest02637(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})

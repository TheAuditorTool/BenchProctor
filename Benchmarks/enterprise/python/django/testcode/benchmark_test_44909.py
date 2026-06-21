# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest44909(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    requests.get(str(data))
    return JsonResponse({"saved": True})

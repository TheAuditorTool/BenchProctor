# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest22716(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})

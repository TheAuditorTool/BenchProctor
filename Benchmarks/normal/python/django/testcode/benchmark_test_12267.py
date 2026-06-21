# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest12267(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})

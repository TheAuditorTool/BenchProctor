# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest15233(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    requests.get(str(data))
    return JsonResponse({"saved": True})

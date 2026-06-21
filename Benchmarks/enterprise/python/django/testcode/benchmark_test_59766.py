# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest59766(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    json.loads(data)
    return JsonResponse({"saved": True})

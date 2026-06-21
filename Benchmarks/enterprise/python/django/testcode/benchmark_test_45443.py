# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest45443(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    json.loads(data)
    return JsonResponse({"saved": True})

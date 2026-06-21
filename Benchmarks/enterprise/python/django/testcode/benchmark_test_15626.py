# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest15626(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})

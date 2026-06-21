# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest34438(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})

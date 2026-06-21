# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest50671(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = FormData(payload=auth_header).payload
    json.loads(data)
    return JsonResponse({"saved": True})

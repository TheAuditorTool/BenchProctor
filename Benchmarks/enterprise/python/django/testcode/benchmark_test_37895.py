# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest37895(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest17966(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

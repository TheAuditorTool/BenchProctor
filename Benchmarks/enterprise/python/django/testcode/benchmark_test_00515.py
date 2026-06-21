# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest00515(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)

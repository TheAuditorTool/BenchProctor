# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest74614(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})

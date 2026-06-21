# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest01887(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})

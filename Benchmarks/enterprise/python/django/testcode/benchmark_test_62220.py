# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest62220(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})

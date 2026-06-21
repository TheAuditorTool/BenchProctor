# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest65211(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})

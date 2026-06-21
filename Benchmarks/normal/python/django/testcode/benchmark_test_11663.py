# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest11663(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

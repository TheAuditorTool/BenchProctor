# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest14591(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    json.loads(data)
    return JsonResponse({"saved": True})

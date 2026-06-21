# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest48136(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    requests.get(str(data))
    return JsonResponse({"saved": True})

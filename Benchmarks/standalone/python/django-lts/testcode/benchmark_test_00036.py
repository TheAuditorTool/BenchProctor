# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00036(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    form = FormData(payload=api_value)
    data = form.payload
    requests.get(str(data))
    return JsonResponse({"saved": True})

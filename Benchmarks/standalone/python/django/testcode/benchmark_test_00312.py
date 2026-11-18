# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import requests
import base64
import pickle


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00312(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    form = FormData(payload=api_value)
    data = form.payload
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import requests
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest26965(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = FormData(payload=api_value).payload
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})

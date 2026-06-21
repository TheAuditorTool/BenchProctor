# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest31461(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = ensure_str(api_value)
    json.loads(data)
    return JsonResponse({"saved": True})

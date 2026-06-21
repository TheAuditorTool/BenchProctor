# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest66331(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import os


def BenchmarkTest55152(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def relay_value(value):
    return value

def BenchmarkTest33556(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = relay_value(dotenv_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest42191(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = str(dotenv_value).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

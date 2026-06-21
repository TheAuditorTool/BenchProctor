# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest10665(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = ' '.join(str(dotenv_value).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

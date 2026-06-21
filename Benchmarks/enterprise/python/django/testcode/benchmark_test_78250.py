# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest78250(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = f'{dotenv_value}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

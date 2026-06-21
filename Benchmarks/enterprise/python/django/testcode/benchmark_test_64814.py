# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest64814(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % str(dotenv_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})

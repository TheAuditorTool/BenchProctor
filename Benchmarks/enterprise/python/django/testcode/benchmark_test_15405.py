# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest15405(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    if api_value:
        data = api_value
    else:
        data = ''
    requests.get(str(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import requests


def BenchmarkTest46268(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = api_value if api_value else 'default'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

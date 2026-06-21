# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import requests


def BenchmarkTest34365(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    def normalize(value):
        return value.strip()
    data = normalize(api_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

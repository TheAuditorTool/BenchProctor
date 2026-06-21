# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import requests


def BenchmarkTest67355(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = (lambda v: v.strip())(api_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

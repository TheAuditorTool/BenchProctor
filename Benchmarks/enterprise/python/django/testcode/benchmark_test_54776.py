# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import requests


def BenchmarkTest54776(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    prefix = ''
    data = prefix + str(api_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

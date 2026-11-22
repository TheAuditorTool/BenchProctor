# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import requests


def BenchmarkTest00002(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = json.loads(api_value).get('value', '')
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)

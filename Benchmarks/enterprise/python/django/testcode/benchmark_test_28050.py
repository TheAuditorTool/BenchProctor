# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import requests


def BenchmarkTest28050(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = ' '.join(str(api_value).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

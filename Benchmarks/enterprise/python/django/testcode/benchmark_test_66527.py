# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import requests


def BenchmarkTest66527(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    kind = 'json' if str(api_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = api_value
            data = parsed
        case _:
            data = api_value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest00040(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = (lambda v: v.strip())(json_value)
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)

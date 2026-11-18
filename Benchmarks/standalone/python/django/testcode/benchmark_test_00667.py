# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest00667(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest34773(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def relay_value(value):
    return value

def BenchmarkTest02182(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = relay_value(forwarded_ip)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

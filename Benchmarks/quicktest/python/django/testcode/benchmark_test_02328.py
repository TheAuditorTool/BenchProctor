# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def normalise_input(value):
    return value.strip()

def BenchmarkTest02328(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = normalise_input(origin_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

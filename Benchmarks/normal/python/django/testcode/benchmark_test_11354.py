# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def to_text(value):
    return str(value).strip()

def BenchmarkTest11354(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = to_text(origin_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

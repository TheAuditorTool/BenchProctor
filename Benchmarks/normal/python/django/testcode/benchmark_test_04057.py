# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest04057(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

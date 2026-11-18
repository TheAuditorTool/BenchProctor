# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00402(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

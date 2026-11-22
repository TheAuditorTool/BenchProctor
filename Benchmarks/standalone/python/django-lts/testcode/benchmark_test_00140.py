# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00140(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

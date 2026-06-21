# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest13227(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    yaml.load(ua_value, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

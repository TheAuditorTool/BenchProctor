# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00514(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

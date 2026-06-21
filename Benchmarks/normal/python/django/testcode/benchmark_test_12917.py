# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12917(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})

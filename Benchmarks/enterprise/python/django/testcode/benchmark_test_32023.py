# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32023(request, path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})

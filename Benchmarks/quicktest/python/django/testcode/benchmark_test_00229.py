# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00229(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})

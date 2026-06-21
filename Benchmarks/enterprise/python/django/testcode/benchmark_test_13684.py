# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13684(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})

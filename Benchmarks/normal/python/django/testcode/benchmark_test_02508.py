# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02508(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})

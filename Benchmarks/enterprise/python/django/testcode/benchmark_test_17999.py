# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17999(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})

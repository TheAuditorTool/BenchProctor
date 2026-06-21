# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07411(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
